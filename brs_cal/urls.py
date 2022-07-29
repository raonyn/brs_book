from django.urls import path, include


from django.contrib.auth import views as auth_views
from . import views

app_name = 'brs_cal'

urlpatterns = [
    path('index', views.index, name="cal"),
]


'''''
urlpatterns = [
    path('', views.index, name="main"),
    path('viewSeat', views.viewSeat, name="seat"),
    path('checkSeat', views.checkSeat, name="checkSeat"),
    path('cancelSeat', views.cancelSeat, name="cancelSeat"),
    path('save/', views.saveData, name="saveData"),

    path('login', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('register', views.register, name="register"),


    path('data', views.data, name="data"),
]

'''