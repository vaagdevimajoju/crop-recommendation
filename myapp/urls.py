from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('get-weather/', views.get_weather, name='get_weather'),
    path('crop/<str:crop_name>/', views.crop_detail, name='crop_detail'),
]