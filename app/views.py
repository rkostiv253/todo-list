from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from app.models import Tag, Task
from app.forms import TaskForm


class TagListView(generic.ListView):
    model = Tag
    template_name = "app/tag_list.html"
    context_object_name = "tag_list"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")
    template_name = "app/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")
    template_name = "app/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")
    template_name = "app/tag_form.html"


class TaskListView(generic.ListView):
    model = Task
    template_name = "app/task_list.html"
    context_object_name = "task_list"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task-list")
    template_name = "app/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task-list")
    template_name = "app/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:task-list")
    template_name = "app/task_confirm_delete.html"


class ToogleTaskStatus(generic.UpdateView):
    model = Task

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = not task.status
        task.save(update_fields=["status"])
        return HttpResponseRedirect(reverse_lazy("app:task-list"))
