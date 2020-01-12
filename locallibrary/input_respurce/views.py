from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import student_data
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_list(request):
    context = {'employee_list': student_data.objects.using('student_meta').all()}
    return render(request, "user_register/employee_list.html", context)


# Create your views here.

"""
@login_required
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            employee = student_data.objects.get(pk=id)
            form = UserForm(instance=employee)
        return render(request, "user_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            employee = student_data.objects.get(pk=id)
            form = UserForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/home/user/list')


def employee_delete(request,id):
    employee = student_data.objects.get(pk=id)
    employee.delete()
    return redirect('/home/user/list')

"""