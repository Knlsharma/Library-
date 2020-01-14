from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)



def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/home/book/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/home/book/list')

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']
        print(srch)
        if srch:
            match = Employee.objects.filter( Q(Bookname__icontains=srch) |
                                         Q(Authorname__icontains=srch)                                                   
                                                   )

            print(match)   

            form = EmployeeForm(instance=match)                                      

            if match:
                return render(request, "employee_register/search.html", {'form': form})
            else:
                messages.error(request , 'no result found')

        else:
            return redirect('/home/book/search/')        
                    
    return render(request ,'employee_register/search.html')                                                 


    
