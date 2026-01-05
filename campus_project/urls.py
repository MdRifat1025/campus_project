
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',include('students.urls')),
    path('accounts/',include('accounts.urls')),
    path('teacher/',include('teacher.urls')),
    path('courses/',include('courses.urls')),
    path('attendance/',include('attendance.urls')),
]
