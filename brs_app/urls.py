from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:post_id>/', views.detail, name='detail'),
#    path('new/', brs_app.views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
#    path('edit/<int:post_id>/', brs_app.views.edit, name='edit'),
    path('update/<int:post_id>/', views.update, name='update'),
]
