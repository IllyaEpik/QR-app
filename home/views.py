from django.shortcuts import render

# Create your views here.
def view_home(request):
    name = request.user
    return render(request,template_name= "home/index.html", context={"name": name})