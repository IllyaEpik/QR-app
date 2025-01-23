from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError
# Create your views here.

def authorization(request):
        error = ""
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username= username, password = password)
            if user:
                login(request, user)
                return redirect('welcome')
            else:
                error = "Username or password is not correct"
        
        return render(request,template_name= "user/authorization.html", context={"error": error})
    
def registration(request):
    add = ""
    if request.method == "POST":
        try:
    
            username= request.POST.get("username")
            password= request.POST.get("password")
            email = request.POST.get("email")
            print(username,password)
            User.objects.create_user( username=username, password=password,email=email)
        except IntegrityError:

            add = "Username already excists"
    return render(request,template_name= "user/registration.html", context={"add": add})

def logout(request):
    if request.user:
        logout(request)
        return redirect('login')

