from django.utils import timezone

from django.core.exceptions import ValidationError
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    STATUS_CHOICES = (
        (True, "Done"),
        (False, "Not done"),
    )
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["status", "-created_at"]

    def clean(self):
        if self.deadline < timezone.now():
            raise ValidationError("Deadline cannot be in the past.")

    def __str__(self):
        return f"{self.name}, {self.content}"
