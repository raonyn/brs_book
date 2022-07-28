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
from django.urls import path
from pip import main

import account.views
import brs_app.views
  
urlpatterns = [
    path('brsadm/', admin.site.urls),
    path('', brs_app.views.index, name='index'),
    path('login/', account.views.login, name='login'),
    path('signup/', account.views.signup, name='signup'),
    path('logout/', account.views.logout, name='logout'),
    path('detail/<int:post_id>/', brs_app.views.detail, name='detail'),
    path('new/', brs_app.views.new, name='new'),
    path('create/', brs_app.views.create, name='create'),
    path('delete/<int:post_id>/', brs_app.views.delete, name='delete'),
]
