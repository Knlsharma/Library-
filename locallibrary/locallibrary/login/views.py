from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.
def index(request):

    if request.method == 'POST':
        name =   request.POST['l_username']
        passwor = request.POST['l_pass']
        user = auth.authenticate(username = name , password = passwor)

        if user is not None:
             auth.login(request,user)
             return redirect('/') 
        else:
             messages.info(request, 'Invalid User')  
             return redirect('/login') 

    else:
        return render(request , "index.html")