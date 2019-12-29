from django.db import models

# Create your models here.

class Employee(models.Model):
   
    Bookname =    models.CharField(max_length=20)
    Authorname =  models.CharField(max_length=20)
    Subjectname = models.CharField(max_length=20)
    Inventory =   models.IntegerField()
    
