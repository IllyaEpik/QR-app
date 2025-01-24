from django.contrib import admin
from django.urls import path
from user.views import authorization,registration,logout_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('authorization/',view=authorization, name="auth"),
    path('registration/', view=registration, name="reg"),
    path('logout',view=logout_user,name='logout')
]