from django.shortcuts import render
from user.models import Profile
from django.shortcuts import redirect
from django.core.handlers.wsgi import WSGIRequest
from  QR_cods.models import QR_CODE


# Create your views here.
def view_subscriptions(request:WSGIRequest):
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
    return render(request,template_name= "subscriptions/index.html", context={'subscription':subscription})
def redirection(request:WSGIRequest, id):
    qr = QR_CODE.objects.get(id = id)
    if qr.blocked:
        return qr.url
    else:
        return 