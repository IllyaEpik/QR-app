from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
import json,os 

# {
#     "phone_number":"+3802352552",
#     "phone_look":"+380-235-2552",
#     "gmail":"like@gmail.com",
#     "telegram":"t.me",
#     "instagram":"https://www.instagram.com/",
#     "facebook":"https://www.facebook.com/?locale=ru_RU",
#     "X or twiter":"https://twitter.com/"
# }
# Create your views here.
def view_contacts(request:WSGIRequest):
    json1 = json.load(open(os.path.abspath(__file__+'/../../user.json')))
    print()
    return render(request,template_name= "contacs/index.html",context=json1
                #   {
        # "phone"
        # "phone_number":"+3802352552",
        # "phone_look":"+380-235-2552",
        # "gmail":"like@gmail.com",
        # "telegram":"t.me",
        # "instagram":"https://www.instagram.com/",
        # "facebook":"https://www.facebook.com/?locale=ru_RU",
        # "x_or_twiter":"https://twitter.com/"
    # }
)
