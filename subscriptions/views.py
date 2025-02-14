from django.shortcuts import render
from user.models import Profile
from django.shortcuts import redirect
# Create your views here.
def view_subscriptions(request):
    subscription = 'none'
    print(request.user.username,type(request.user))
    # AnonymousUser <class 'django.utils.functional.SimpleLazyObject'>
    if request.method == 'POST':
        if request.user.username:
            profile = Profile.objects.get(user=request.user)
            profile.subcription = request.POST.get('subscription')
            profile.save()
        else:
            return redirect('auth')
    if request.user.username:
        subscription = Profile.objects.get(user=request.user).subcription
    print(subscription)
    return render(request,template_name= "subscriptions/index.html", context={'subscription':subscription})