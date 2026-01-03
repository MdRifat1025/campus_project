from django import forms
from .models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['user','department','semester','phone']
        