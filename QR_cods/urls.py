from .views import *
from django.urls import path
from .views import subscribe
urlpatterns = [
    path('create/',view=render_create_qr_cods,name='create_qr_cods'),
    path('my/',view=render_my_qr_cods, name='my_qr_cods'),
    path("subscribe/", subscribe, name="subscribe")
]