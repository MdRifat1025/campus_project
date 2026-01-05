from django.db import models

from django.conf import settings

class Students(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )
    department=models.CharField(max_length=50)
    semester=models.CharField(max_length=50)
    phone=models.CharField(unique=True,max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"
