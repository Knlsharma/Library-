from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('Bookname','Authorname','Subjectname','Inventory')
        labels = {
            'Bookname':'Book Name',
            'Authorname':'Author Name' ,
             'Subjectname' : 'Subject Name' ,
             'Inventory' :  'Inventory'
        }


"""
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
"""