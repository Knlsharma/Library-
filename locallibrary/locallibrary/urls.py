
from django.urls import path , include
from django.contrib import admin



urlpatterns = [
    path('home/admin', admin.site.urls),
    path('home/login' , include('login.urls')) ,
    path('home/register' , include('register.urls')) , 
    path('home' , include('management.urls')) , 
    path('home/book', include('employee_register.urls')),
]

