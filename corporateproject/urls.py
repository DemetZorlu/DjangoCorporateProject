"""corporateproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('about/', include('home.urls')),
    path('contact/', include('home.urls')),
    path('referances/', include('home.urls')),
    path('academiccalendar/', include('home.urls')),
    path('menucontent/<int:id>/<slug:slug>/', include('home.urls')),
    path('contentdetail/<int:id>/<slug:slug>/', include('home.urls')),
    path('faqs/', include('home.urls')),

]
# Görselin admin panelinde görüntülenmesine ve görsel yoluna adres satırı ile ulaşışmasına sağlıyor.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
