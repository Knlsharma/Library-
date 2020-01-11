from django import forms
from .models import student_data


class UserForm(forms.ModelForm):

    class Meta:
        model = student_data
        fields = ('Sname','Uname','Rollno','Avgmarks' , 'Phno')
        labels = {
            'Sname':'Name',
            'Uname':'User Name' ,
            'Rollno' : 'Roll No.' ,
            'Avgmarks' :  'Avg. Marks' ,
             'Phno' :  'Phone No.'
        }


"""
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
"""