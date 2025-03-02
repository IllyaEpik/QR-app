from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from .models import Profile
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.

def authorization(request:WSGIRequest):
        error = ""
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username= username, password = password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                error = "Username or password is not correct"
        
        return render(request,template_name= "user/authorization.html", context={"error": error})
    
def registration(request:WSGIRequest):
    add = ""
    if request.method == "POST":
        try:
    
            username= request.POST.get("username")
            password= request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            email = request.POST.get("email")
            if password == confirm_password:
                user = User.objects.create_user( username=username, password=password,email=email)
                Profile.objects.create(user=user,subcription='free',desktop_QR = 0)
            else:
                add = "passwords don't match"
        except IntegrityError:

            add = "Username already excists"
    return render(request,template_name= "user/registration.html", context={"add": add})

def logout_user(request:WSGIRequest):
    logout(request)
    return redirect('auth')

