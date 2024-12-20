from django.shortcuts import render

# Create your views here.
def view_contacts(request):
    return render(request,template_name= "contacts/index.html")
