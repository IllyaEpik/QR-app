from django.contrib import admin
from django.urls import path
from user.views import authorization,registration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('authorization/',view=authorization, name="auth"),
    path('registration/', view=registration, name="reg")
]