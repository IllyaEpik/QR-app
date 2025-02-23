from django.shortcuts import render
from user.models import Profile
from django.shortcuts import redirect
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
def view_home(request:WSGIRequest):
    subscription = 'none'
    if request.method == 'POST':
        if request.user.username:
            profile = Profile.objects.get(user=request.user)
            profile.subcription = request.POST.get('subscription')
            profile.save()
        else:
            return redirect('auth')
    if request.user.username:
        subscription = Profile.objects.get(user=request.user).subcription
    return render(request,template_name= "home/index.html", context={'subscription':subscription})