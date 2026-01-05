from django.db import models
from teacher.models import Teacher
from students.models import Students

class Attendance(models.Model):
    student=models.ForeignKey(Students, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    # status=models.BooleanField(default=False)
    status=models.CharField(max_length=10,choices=(('present','present'),('absent','absent')))

    def __str__(self):
        return f"{self.student} - {self.teacher} - {self.date} - {self.status}"
