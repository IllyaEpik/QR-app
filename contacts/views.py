from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def view_contacts(request:WSGIRequest):
    return render(request,template_name= "contacs/index.html")
