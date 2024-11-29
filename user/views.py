from django.shortcuts import render

# Create your views here.

def authorization(request):
    return render(request,template_name= "user/authorization.html")
    
def registration(request):
    return render(request,template_name= "user/registration.html")

