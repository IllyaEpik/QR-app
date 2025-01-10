from django.shortcuts import render

# Create your views here.
def view_subscriptions(request):
    return render(request,template_name= "subscriptions/index.html")