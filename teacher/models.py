from django.db import models
from django.conf import settings

class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'}
    )
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
