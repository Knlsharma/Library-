from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def index(request):

    if request.method == 'POST':
        name =   request.POST['l_username']
        passwor = request.POST['l_pass']
        user = auth.authenticate(username = name , password = passwor)

        if user is not None:
             auth.login(request,user)
             return redirect('/home') 
        else:
             messages.info(request, 'Invalid User')  
             return redirect('/login') 

    else:
        return render(request , "index.html") 

def signout(request):
    logout(request)
    return redirect('/home/login')    