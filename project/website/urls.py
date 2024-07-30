from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mapa/', views.mapa, name='mapa'),
    path('audiencias/', views.mapa, name='audiencias'),
]    