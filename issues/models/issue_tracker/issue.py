from django.db import models
from issues.models.issue_tracker.base_model import BaseModel
from issues.models.issue_tracker.type import Type
from issues.models.issue_tracker.status import Status
from issues.models.validators import NoUpperCaseValidator,MinWordsValidators
from issues.models.projects.project import Project

class Issue(BaseModel):
    summary = models.CharField(
        max_length=300,
        verbose_name="краткое описание",
        validators=[NoUpperCaseValidator(1)]
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="полное описание",
        validators=[MinWordsValidators(5)]
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="статус")
    types = models.ManyToManyField(Type, verbose_name="типы", blank=True, related_name="issues")
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="проект",
        related_name="issues",
    )

    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"

