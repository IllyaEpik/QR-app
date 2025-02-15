from .views import *
from django.urls import path
from .views import delete_qr_code
from .views import filter_qr_codes
urlpatterns = [
    path('create',view=render_create_qr_cods,name='create_qr_cods'),
    path('my/',view=render_my_qr_cods, name='my_qr_cods'),
    path('delete/<int:qr_id>/', delete_qr_code, name='delete_qr'),
    path("filter/", filter_qr_codes, name="filter_qr_codes"),
]