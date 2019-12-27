from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages


# Create your views here.


def register(request):
 
    if request.method == 'POST' :

            name =   request.POST['username']
            ph1 =    request.POST['ph']
            email1 = request.POST['email']
            pass12 = request.POST['pass1']
            pass123 = request.POST['pass2']
    
            if pass12 == pass123 :
                    if User.objects.filter(username=name).exists():
                        messages.info(request, 'Username Already Taken !!')
                        return render(request , "register.html")  
                    elif User.objects.filter(email=email1).exists():
                        messages.info(request, 'Email Already Taken')
                        return render(request , "register.html")  
                    else:                      
                        new_user = User.objects.create_user(username = name , email= email1 ,password=pass12 )
                        new_user.save()
                        print('new user created')            
                        return redirect("/login")           

            else:
                messages.info(request, 'Password Not Matching...')
                return render(request , "register.html") 

    else:
            
            return render(request , "register.html")            