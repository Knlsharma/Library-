from django.db import models

# Create your models here.

class Meta:
        app_label = 'student_meta'

class student_data(models.Model):
   
    Sname =    models.CharField(max_length=20)
    Uname =    models.CharField(max_length=20)
    Rollno =  models.IntegerField()
    Avgmarks = models.IntegerField()
    Phno =   models.IntegerField()
    



