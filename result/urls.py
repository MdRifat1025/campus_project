from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_result, name='add_result'),
    path('view/', views.view_result, name='view_result'),
]
