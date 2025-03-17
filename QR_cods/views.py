from django.shortcuts import render, get_object_or_404, redirect
from .models import QR_CODE
from user.models import Profile
from QR_app.settings import MEDIA_URL
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
import qrcode, os
import matplotlib.colors as mc
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
import base64, io
from django.shortcuts import render, redirect

def create_qr_code(request:WSGIRequest,error = False):
    
    filename = os.path.join(f"{request.user.username}/{request.POST.get('name')}.png")
    path = os.path.abspath(__file__+f'/../../media/images/qr_code/{filename}')
    file = None
    # Якщо не створена папка media/qr_code/username
    try:
        os.mkdir(os.path.abspath(path+'/..'))
    except:
        pass
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    # Якщо користувач натиснув на create
    if request.POST.get('button') == 'create':
        profile = Profile.objects.get(user = request.user)
        desktop = False
        if request.POST.get("type-qr") == "desktop" and profile.desktop_QR > 0:
            desktop = True
        img = QR_CODE.objects.create(profile = request.user,
            name = request.POST.get('name'),
            qr_code = filename,
            description = '',
            url = request.POST.get('url'),
            desktop = desktop,
            blocked = False
        )
        file = img.qr_code
        img.save()
        # Якщо користувач створюе  desktop QR-code
        if request.POST.get("type-qr") == "desktop" and profile.desktop_QR > 0:
            qr.add_data(request.POST.get('url'))
            profile.desktop_QR -= 1
            profile.save()
        else:
            # Якщо користувач створюе не desktop QR-code
            qr.add_data(request.build_absolute_uri(reverse("redirection",kwargs={'qr_id': img.id})))
    else:
        # Якщо користувач натиснув на check
        qr.add_data('no no no mrFish')
    qr.make(fit=True)
    # Якщо у користувача підписка free
    if error:
        img = qr.make_image(fill_color='black',back_color='white').convert('RGB')
        ok = io.BytesIO()
        img.save(ok,format="PNG")
        filename = base64.b64encode(ok.getvalue()).decode("utf-8")
    else:
        # Якщо користувач створюе кольоровий QR-code
        if request.POST.get("type") == "color":
            img = qr.make_image(fill_color=request.POST.get('color'), back_color=request.POST.get('background_color')).convert('RGB')
            if request.POST.get('button') == 'check':
                ok = io.BytesIO()
                img.save(ok,format="PNG")
                filename = base64.b64encode(ok.getvalue()).decode("utf-8")
        # Якщо користувач створюе градіентний  QR-code
        else:
            color3 = (0,0,0)
            ok = mc.to_rgb(request.POST.get('background_color'))
            if ok[0]+ok[1]+ok[2] < 1.5:
                color3 = (255,255,255)
            # Створюємо черно-білий QR-code
            img = qr.make_image(fill_color=color3,back_color=request.POST.get('background_color')).convert('RGB')
            size = img.width
            color1 = mc.to_rgb(request.POST.get("color"))
            color2 = mc.to_rgb(request.POST.get("color_2"))
            color1 = (color1[0]*255,color1[1]* 255,color1[2]* 255)
            color2 = (color2[0]* 255,color2[1]* 255,color2[2]* 255)
            # 
            for h in range(size):
                for w in range(size):
                    # перевірка чи піксель не фоновий колір
                    if img.getpixel((w,h)) == color3:
                        # обчислення червоного кольору
                        r = int(color1[0] + (color2[0] - color1[0]) * w / size)
                        # обчислення зеленого кольору
                        g = int(color1[1] + (color2[1] - color1[1]) * w / size)
                        # обчислення синього кольору
                        b = int(color1[2] + (color2[2] - color1[2]) * w / size)
                        # заміна пікселя на інший піксель,який створений в в r,g,b
                        img.putpixel((w,h),(r,g,b))
            ok = io.BytesIO()
            img.save(ok,format="PNG")
            filename = base64.b64encode(ok.getvalue()).decode("utf-8")
    # Створює QR-code з логотипом 
    if 'logo' in request.FILES and not error:
        # Отримуемо картинку 
        logo = Image.open(request.FILES.get('logo'))
        data = logo.getdata()
        # Отримуемо колір заднього фону 
        color = []
        for c in mc.to_rgb(request.POST.get('background_color')):
            color.append(int(c*255))
        color = (color[0],color[1],color[2])
        # Заміняемо всі прозрачні та чорні піксулі на піксулі заднього фону 
        new_data = []
        try:
            for item in data:
                if item[3] == 0:
                    new_data.append(color)
                else:
                    new_data.append(item)
        except:
            for item in data:
                new_data.append(item)
        logo.putdata(new_data)
        qr_width, qr_height = img.size
        logo_size = qr_width // 4
        logo = logo.resize((logo_size, logo_size))

        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        # Переносимо картинку на QR-code,
        img.paste(logo, pos)
    if request.POST.get('button') == 'create':
        img.save(path) 
    if file:
        filename = file
    return filename
def render_create_qr_cods(request:WSGIRequest):
    error = ''
    name = None
    try:
        profile = Profile.objects.get(user = request.user)
        subscription = profile.subcription
        QR = Profile.objects.get(user =  request.user).desktop_QR
    except:
        profile = None
        subscription = None
        QR = '0'
        
    if request.method == "POST" and profile:
        if len(QR_CODE.objects.filter(name = request.POST.get('name'),profile=request.user)):
            error = "Qr-code with this name been created, you can't create two QR codes with same name"
        else:
            if request.POST.get("type-qr") != 'desktop':
                count = len(QR_CODE.objects.filter(profile=request.user,desktop = False))
                subscription = profile.subcription
                if count > 0 and subscription == "free":
                    error = 'you cannot have more qr codes, it is limit of your subscription'
                elif count > 9 and subscription == "standart":
                    error = 'you cannot have more qr codes, it is limit of your subscription'
                elif count > 99 and subscription == "pro":
                    error = 'you cannot have more qr codes, it is limit of your subscription'
                else:
                    if subscription == "free":
                        name = create_qr_code(request,error=True) 
                    else:
                        name = create_qr_code(request)
            else:

                if profile.desktop_QR > 0:
                    name = create_qr_code(request)
                else:
                    error = "you don't have desktop QR-codes"

    url = True
    if request.POST.get('button') == 'check':
        url = False
    return render(request, template_name='create_QR_cods.html' ,context={
        'name':name,
        'error':error,
        'MEDIA_URL':MEDIA_URL,
        "url":url,
        'subcription':subscription,
        'desktop_QR': QR
                }) 
def render_my_qr_cods(request:WSGIRequest):
    modal = None
    pk = request.user.pk
    qr_codes = []
    if pk:
        qr_codes = QR_CODE.objects.filter(profile = request.user)
    if request.method == "POST":
        if not request.POST.get("name"):
            modal = request.POST.get("id")

            modal = QR_CODE.objects.get(id = modal)
            
        elif request.POST.get("del"):
            delete = QR_CODE.objects.get(id=request.POST.get("del"))
            try:
                os.remove(os.path.abspath(__file__+'/../..'+MEDIA_URL+'images/qr_code/'+delete.qr_code.name))
            except:
                pass
            delete.delete()
        else:
            qr_code = QR_CODE.objects.get(id = request.POST.get("id"))
            qr_code.name = request.POST.get("name")
            qr_code.description = request.POST.get("description")
            qr_code.save()

    return render(request, template_name='my_QR_cods.html',context={
        'qr_codes':qr_codes,
        'MEDIA_URL':MEDIA_URL,
        'modal': modal,
        'pk':pk

    })

