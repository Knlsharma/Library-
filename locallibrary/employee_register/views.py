from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


@login_required
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

@login_required
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/home/book/list')

def search(request):
    if 'search' in request.GET:
      search_term = request.GET['search']
      context = Employee.objects.all().filter(icontains=search_term) 
      return render(request, "employee_register/search.html", context)
    

    """
    context = { 'search': Employee.objects.all() }
    return render(request, "employee_register/search.html", context)


    
    model = Employee
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Employee.objects.filter(name__contains=search)
          print(postresult)
          result = postresult
       else:
           result = None
       return result
   

    return render(request, "employee_register/search.html")
    """
      




    
