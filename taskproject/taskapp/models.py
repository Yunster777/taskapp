from django.db import models
from django.utils.translation import gettext_lazy as _  # django의 다국어 처리 기능과 연동 가능


class Task(models.Model):
    class TaskTypes(models.TextChoices):
        JOB = "JOB", _("업무")
        HEALTH = "HEALTH", _("건강")
        SOCIAL = "SOCIAL", _("사회")

    title = models.CharField(max_length=50, null=False)
    type = models.CharField(
        choices=TaskTypes.choices,
        max_length=10,
        default=TaskTypes.JOB,
    )
    due = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title


class ChecklistItem(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, null=False)
    checked = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.content
