from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Role choices
    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ADMIN)
    
    def __str__(self):
        return f"{self.username} - {self.role}"