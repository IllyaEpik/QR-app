from django.shortcuts import render
from .models import QR_CODE
from user.models import Profile
from QR_app.settings import MEDIA_URL
import qrcode, os
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
    )
    qr.add_data(request.POST.get('url'))
    qr.make(fit=True)
    if error:
        img = qr.make_image(fill_color='black',back_color='white')
    else:
        img = qr.make_image(fill_color=request.POST.get('color'), back_color=request.POST.get('background_color'))
    if request.POST.get('button') == 'create':
        img.save(path) 
        img = QR_CODE.objects.create(profile = request.user,
                            name = request.POST.get('name'),
                            qr_code = filename,
                            description = '')
    if 'logo' in request.FILES:
        logo_file = request.FILES['logo']
        logo_path = default_storage.save(f"logos/{logo_file.name}", ContentFile(logo_file.read()))
        logo_full_path = os.path.join(settings.MEDIA_ROOT, logo_path)

        logo = Image.open(logo_full_path)

        qr_width, qr_height = img.size
        logo_size = qr_width // 4
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        img.paste(logo, pos, mask=logo)

    filename = f"qr_{request.POST.get('name')}.png"
    path = os.path.join(settings.MEDIA_ROOT, "qrcodes", filename)
    img.save(path)

    qr_code = QR_CODE.objects.create(
        profile=request.user,
        name=request.POST.get('name'),
        description=""
    )
    
    return filename
# Create your views here.
def render_create_qr_cods(request):
    error = ''
    name = None
    if request.method == "POST":
        # try:
            if len(QR_CODE.objects.filter(name = request.POST.get('name'),profile=request.user)):
                pass
            else:
                try:
                    name = create_qr_code(request)
                except:
                    name = create_qr_code(request,error=True)
        # except Exception as error:
        #     error = 'error creating qrcode'
        #     # pass
    return render(request, template_name='create_QR_cods.html' ,context={
        'name':name,
        'error':error,
        'MEDIA_URL':MEDIA_URL
    })
def render_my_qr_cods(request):
    qr_codes = QR_CODE.objects.filter(profile = request.user)
    return render(request, template_name='my_QR_cods.html',context={
        'qr_codes':qr_codes,
        'MEDIA_URL':MEDIA_URL
    })