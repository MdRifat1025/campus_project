from django.db import models
from teacher.models import Teacher

from students.models import Students

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Students, blank=True)

    def __str__(self):
        return self.name
