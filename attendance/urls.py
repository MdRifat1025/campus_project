from django.urls import path
from . import views

urlpatterns = [
    path('take/', views.take_attendance, name='take_attendance'),
    path('view/', views.view_attendance, name='view_attendance'),
]
