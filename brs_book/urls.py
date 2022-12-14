"""brs_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path, include
from pip import main

import account.views
import brs_app.views
import brs_cal.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('brsadm/', admin.site.urls),
    path('', brs_app.views.index, name='index'),
    path('login/', account.views.login, name='login'),
    path('signup/', account.views.signup, name='signup'),
    path('logout/', account.views.logout, name='logout'),
    path('brs_app/', include('brs_app.urls')),
    path('brs_cal/', include('brs_cal.urls')),
    path('calendar', brs_cal.views.main, name='calendar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
