from django.shortcuts import render, redirect
from .models import Attendance
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required

# Teacher takes attendance
@login_required
def take_attendance(request):
    user = request.user
    if not hasattr(user, 'teacher'):
        return redirect('dashboard')  # Only teacher can access

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.teacher = user.teacher
            attendance.save()
            return redirect('take_attendance')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/take_attendance.html', {'form': form})

# Student views their own attendance
@login_required
def view_attendance(request):
    user = request.user
    if not hasattr(user, 'student'):
        return redirect('dashboard')  # Only student can access

    attendance_records = Attendance.objects.filter(student=user.student)
    return render(request, 'attendance/view_attendance.html', {'attendance_records': attendance_records})
