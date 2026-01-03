from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Students
from .forms import StudentsForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the students index.")  

@login_required
def student_list(request):
    students=Students.objects.all()
    return render(request,"student_list.html",{'students':students})
@login_required
def student_create(request):
    form=StudentsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request,"student_form.html",{'form':form})

def student_update(request,pk):
    students=get_object_or_404(Students,pk=pk)
    # student=Students.objects.get(pk=pk)
    form=StudentsForm(request.POST or None,instance=students)
    if form.is_valid():
        form.save()
        return redirect("student_list")

    return render(request,"student_form.html",{'form':form})

def student_delete(request,pk):
    students=get_object_or_404(Students,pk=pk)
    # student=Students.objects.get(pk=pk)
    if request.method=="POST":
        students.delete()
        return redirect("student_list")

    return render(request,"student_confirm_delete.html")