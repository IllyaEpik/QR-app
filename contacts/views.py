from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
import json,os 


# Create your views here.
def view_contacts(request:WSGIRequest):
    # отримуємо дані з json
    json1 = json.load(open(os.path.abspath(__file__+'/../../user.json')))

    return render(request,template_name= "contacs/index.html",context=json1
)