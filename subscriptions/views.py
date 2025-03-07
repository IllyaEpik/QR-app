from django.shortcuts import render
from user.models import Profile
from django.shortcuts import redirect
from django.core.handlers.wsgi import WSGIRequest
from  QR_cods.models import QR_CODE


ok = {
    'standart':10,
    'pro':100,
    'free':1
}
# Create your views here.
def view_subscriptions(request:WSGIRequest):
    global ok
    subscription = 'none'
    if request.method == 'POST':
        if request.user.username:
            profile = Profile.objects.get(user=request.user)
            sub = request.POST.get('subscription')
            if not ';' in sub:
                profile.subcription = sub
                count = ok[sub]

                for qr in QR_CODE.objects.filter(profile = request.user,desktop = False):
                    if count > 0:
                        count -= 1
                        if qr.blocked:
                            qr.blocked = False
                            qr.save()
                    else:
                        qr.blocked = True
                        qr.save()
            else:
                print(sub.split(';')[1])
                profile.desktop_QR += int(sub.split(';')[1])
            profile.card_number = request.POST.get('card')
            profile.CVV = request.POST.get('CVV')
            # desktop_QR
            profile.save()
            
        else:
            return redirect('auth')
    if request.user.username:
        subscription = Profile.objects.get(user=request.user).subcription
    return render(request,template_name= "subscriptions/index.html", context={'subscription':subscription})
def redirection(request:WSGIRequest, qr_id):
    print(QR_CODE.objects.get)
    qr = QR_CODE.objects.get(id = qr_id)
    if qr.blocked:
        return render(request, template_name='subscriptions/block.html')
    else:
        try:
            return redirect(qr.url)
        except:
            return render(request,'subscriptions/copy.html', {'url':qr.url})