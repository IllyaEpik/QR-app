from django.shortcuts import render

# Create your views here.
def render_qr_cods(request):
    return render(request, template_name='QR_cods.html' )
