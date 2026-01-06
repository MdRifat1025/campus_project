from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Result
from .forms import ResultForm

def result_list(request):
    return render(request,'result_list.html')

def add_result(request):
    if not hasattr(request.user, 'teacher'):
        return redirect('dashboard')
    
    if request.method=="POST":
        forms=ResultForm(request.POST)
        if forms.is_valid():
            obj=forms.save(commit=False)
            obj.teacher=request.user.teacher
            obj.save()

            return redirect('add_result')
    else:
        forms=ResultForm()


    return render(request,'result/add_result.html',{'forms':forms})

    



@login_required
def view_result(request):
    if not hasattr(request.user, 'student'):
        return redirect('dashboard')

    results = Result.objects.filter(student=request.user.student)
    return render(request, 'result/view_result.html', {'results': results})