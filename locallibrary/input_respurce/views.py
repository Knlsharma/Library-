from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import student_data
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

from openpyxl import Workbook

import openpyxl

# Create your views here.

@login_required
def user_list(request):
    context = {'employee_list': student_data.objects.using('student_meta').all()}
    return render(request, "user_register/employee_list.html", context)


@login_required
def upload(request):
        if "GET" == request.method:
            return render(request, 'user_register/upload.html' , { })
        else:
            excel_file = request.FILES["document"]

            # you may put validations here to check extension or file size

            wb = openpyxl.load_workbook(excel_file)

            # getting a particular sheet by name out of many sheets
            worksheet = wb["Sheet1"]
            print(worksheet)

            excel_data = list()
            # iterating over the rows and
            # getting value from each cell in row
            for row in worksheet.iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))
                excel_data.append(row_data)
                return render(request, "user_register/upload.html", {"excel_data":excel_data} ) 
    


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