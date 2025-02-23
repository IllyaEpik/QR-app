from django.shortcuts import render
from .models import QR_CODE
from user.models import Profile
from QR_app.settings import MEDIA_URL
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
import qrcode, os
import matplotlib.colors as mc
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
import base64, io
from django.shortcuts import render
# django.core.handlers.wsgi.WSGIRequest
def create_qr_code(request:WSGIRequest,error = False):
    filename = os.path.join(f"{request.user.username}/{request.POST.get('name')}.png")
    path = os.path.abspath(__file__+f'/../../media/images/qr_code/{filename}')
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
    qr.add_data(request.POST.get('url'))
    qr.make(fit=True)
    
    if error:
        img = qr.make_image(fill_color='black',back_color='white').convert('RGB')
    else:
        if request.POST.get("type") == "color":
            img = qr.make_image(fill_color=request.POST.get('color'), back_color=request.POST.get('background_color')).convert('RGB')

        else:
            color3 = (0,0,0)
            ok = mc.to_rgb(request.POST.get('background_color'))
            if ok[0]+ok[1]+ok[2] < 1.5:
                color3 = (255,255,255)
            img = qr.make_image(fill_color=color3,back_color=request.POST.get('background_color')).convert('RGB')
            size = img.width
            color1 = mc.to_rgb(request.POST.get("color"))
            color2 = mc.to_rgb(request.POST.get("color_2"))
            color1 = (color1[0]*255,color1[1]* 255,color1[2]* 255)
            color2 = (color2[0]* 255,color2[1]* 255,color2[2]* 255 )
            for h in range(size):
                for w in range(size):
                    
                    if img.getpixel((w,h)) == color3:
                        r = int(color1[0] + (color2[0] - color1[0]) * w / size)
                        g = int(color1[1] + (color2[1] - color1[1]) * w / size)
                        b = int(color1[2] + (color2[2] - color1[2]) * w / size)
                        img.putpixel((w,h),(r,g,b))
    if 'logo' in request.FILES and not error:
        # logo_file = request.FILES['logo']
        # logo_path = default_storage.save(f"logos/{logo_file.name}", ContentFile(logo_file.read()))
        # logo_full_path = os.path.join(settings.MEDIA_ROOT, logo_path)

        logo = Image.open(request.FILES.get('logo'))
        data = logo.getdata()

        color = []
        for c in mc.to_rgb(request.POST.get('background_color')):
            color.append(int(c*255))
        color = (color[0],color[1],color[2])
        print(color)
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
        img.paste(logo, pos)
    if request.POST.get('button') == 'create':
        img.save(path) 
        img = QR_CODE.objects.create(profile = request.user,
                            name = request.POST.get('name'),
                            qr_code = filename,
                            description = '')
    else:
        ok = io.BytesIO()
        img.save(ok,format="PNG")
        filename = base64.b64encode(ok.getvalue()).decode("utf-8")
    return filename
# Create your views here.
@login_required  
def render_create_qr_cods(request:WSGIRequest):
    error = ''
    name = None
    if request.method == "POST":
            print(request.POST.get('color'))
        # try:
            
            count = len(QR_CODE.objects.filter(profile=request.user))
            subscription = Profile.objects.get(user = request.user).subcription
            if len(QR_CODE.objects.filter(name = request.POST.get('name'),profile=request.user)):
                error = "Qr-code з таким ім'ям вже був створений"
            elif count > 0 and subscription == "free":
                error = 'you cannot have more qr codes, it is limit of your subscription'
            elif count > 9 and subscription == "standart":
                error = 'you cannot have more qr codes, it is limit of your subscription'
            elif count > 99 and subscription == "pro":
                error = 'you cannot have more qr codes, it is limit of your subscription'
            else:
                if subscription == "free":
                    name = create_qr_code(request,error=True) 
                else:
                    # try:
                        name = create_qr_code(request)
                    # except:
                        # name = create_qr_code(request,error=True)   
              
        # except Exception as error:
        #     error = 'error creating qrcode'
        #     # pass
    url = True
    if request.POST.get('button') == 'check':
        url = False
    return render(request, template_name='create_QR_cods.html' ,context={
        'name':name,
        'error':error,
        'MEDIA_URL':MEDIA_URL,
        "url":url
    })
@login_required
def render_my_qr_cods(request:WSGIRequest):
    print(type(request))
    modal = None
    qr_codes = QR_CODE.objects.filter(profile = request.user)
    if request.method == "POST":
        if not request.POST.get("name"):

            modal = request.POST.get("id")

            modal = QR_CODE.objects.get(id = modal)
            
        elif request.POST.get("del"):
            delete = QR_CODE.objects.get(id=request.POST.get("del"))
            os.remove(os.path.abspath(__file__+'/../..'+MEDIA_URL+'images/qr_code/'+delete.qr_code.name))
            # os.remove(delete.qr_code.path)
            delete.delete()

        else:
            qr_code = QR_CODE.objects.get(id = request.POST.get("id"))
            qr_code.name = request.POST.get("name")
            qr_code.description = request.POST.get("description")
            qr_code.save()
        
    # print(modal)
    return render(request, template_name='my_QR_cods.html',context={
        'qr_codes':qr_codes,
        'MEDIA_URL':MEDIA_URL,
        'modal': modal
    })
