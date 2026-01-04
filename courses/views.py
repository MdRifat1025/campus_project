from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import CourseForm

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/course_form.html', {'form': form})
