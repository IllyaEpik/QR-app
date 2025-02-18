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
import base64, io
from django.shortcuts import render

def filter_qr_codes(request):
    query = request.GET.get("query", "")
    qr_codes = QR_CODE.objects.all()

    if query:
        qr_codes = qr_codes.filter(name__icontains=query)

    return render(request, "qr_codes_list.html", {"qr_codes": qr_codes, "query": query})


def delete_qr_code(request, qr_id):
    qr_code = get_object_or_404(QR_CODE, id=qr_id)
    qr_code.delete()
    return JsonResponse({"message": "QR-код успішно видалено"}, status=200)

def create_qr_code(request,error = False):
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
        img = qr.make_image(fill_color=request.POST.get('color'), back_color=request.POST.get('background_color')).convert('RGB')
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
        for item in data:
            if item[3] == 0:
                new_data.append(color)
            else:
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
def render_create_qr_cods(request):
    error = ''
    name = None
    if request.method == "POST":
            print(request.POST.get('color'))
        # try:
            
            count = len(QR_CODE.objects.filter(profile=request.user))
            subscription = Profile.objects.get(user = request.user).subcription
            # if len(QR_CODE.objects.filter(name = request.POST.get('name'),profile=request.user)):
            #     error = ''
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
def render_my_qr_cods(request):
    qr_codes = QR_CODE.objects.filter(profile = request.user)
    return render(request, template_name='my_QR_cods.html',context={
        'qr_codes':qr_codes,
        'MEDIA_URL':MEDIA_URL
    })
