from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User

# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if not role:
            messages.error(request, "Please select a role")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect("login")

        if user.role != role:
            messages.error(request, "Role does not match this account")
            return redirect("login")

        auth_login(request, user)

        if user.role == "admin":
            return redirect("/admin/")
        else:
            return redirect("dashboard")

    return render(request, "login.html")


# REGISTRATION (optional for teacher/student)
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if role not in ['student', 'teacher']:
            messages.error(request, "Invalid role")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        auth_login(request, user)
        return redirect("login")

    return render(request, "register.html")


# DASHBOARD
@login_required
def dashboard(request):
    if request.user.role == "teacher":
        return render(request, "teacher_db.html")
    elif request.user.role == "student":
        return render(request, "student_db.html")
    else:
        messages.error(request, "You do not have access")
        return redirect("login")


# LOGOUT
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect("login")
