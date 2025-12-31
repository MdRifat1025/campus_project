from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)

            if user.role == "admin":
                return redirect("/admin/")
            else:
                return redirect("dashboard/")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


@login_required
def dashboard(request):
    if request.user.role == "teacher":
        return render(request, "teacher_dashboard.html")
    elif request.user.role == "student":
        return render(request, "student_dashboard.html")
    else:
        messages.error(request, "You do not have access")
        return redirect('login')


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')
