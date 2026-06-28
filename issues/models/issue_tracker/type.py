from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"