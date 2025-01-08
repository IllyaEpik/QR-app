from django.shortcuts import render

# Create your views here.
def render_create_qr_cods(request):
    return render(request, template_name='create_QR_cods.html' )
def render_my_qr_cods(request):
    return render(request, template_name='my_QR_cods.html' )