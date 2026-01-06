from django.db import models
from students.models import Students
from teacher.models import Teacher
from courses.models import Course
class Result(models.Model):
    student=models.ForeignKey(Students,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    courses=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveSmallIntegerField()
    grade=models.CharField(max_length=3)
    date=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=('student','courses')

    def save(self,*args,**kwargs):
        if self.marks>80:
            self.grade='A+'
        elif self.marks>=70:
            self.grade='A'
        elif self.marks>=60:
            self.grade='B'
        elif self.marks>=50:
            self.grade='C'
        elif self.marks>=40:
            self.grade='D'
        else:
            self.grade='F'
        super().save(*args,**kwargs)


def __str__(self):
        return f"{self.student.user.username} - {self.course.name}"

