from django.db import models

class Project(models.Model):
    start_date = models.DateField(blank=False,null=False,verbose_name="дата начала")
    end_date = models.DateField(null=True, blank=True,verbose_name="дата окончания")
    name = models.CharField(max_length=100, verbose_name="название проекта")
    description = models.TextField(max_length=300, verbose_name="описание проекта")

    def __str__(self):
        return self.name
