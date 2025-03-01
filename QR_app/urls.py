"""
URL configuration for QR_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import view_home
from contacts.views import view_contacts
from subscriptions.views import view_subscriptions,redirection
from . import settings
from django.conf.urls.static import static
# from user.urls import 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=view_home),
    path('user/',include("user.urls")),
    path('contacts', view=view_contacts, name="contacts"),
    path('QR_cods/',include("QR_cods.urls")),
    path('subscriptions/',view_subscriptions),
    path('block/', redirection)
    # path('qr_cods/', view=render_qr_cods, name="create_qr_cods"),
    # path('qr_cods/', view=render_qr_cods, name="create_qr_cods")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)