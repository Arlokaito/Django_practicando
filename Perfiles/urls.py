from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio-perfiles'),
    path('formulario/', views.formulario, name='formulario'),
]