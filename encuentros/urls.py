from django.urls import path
from . import views

urlpatterns = [
    path('<int:solicitud_id>/crear/', views.crear_encuentro, name='crear_encuentro'),
    path('<int:solicitud_id>/ver/', views.ver_encuentro, name='ver_encuentro'),
]
