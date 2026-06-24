from django.urls import path
from . import views

urlpatterns = [
    path('<int:libro_id>/solicitar/', views.solicitar_libro, name='solicitar_libro'),
    path('solicitud/<int:solicitud_id>/', views.ver_solicitud, name='ver_solicitud'),
    path('solicitud/<int:solicitud_id>/aceptar/', views.aceptar_solicitud, name='aceptar_solicitud'),
    path('solicitud/<int:solicitud_id>/rechazar/', views.rechazar_solicitud, name='rechazar_solicitud'),
    path('solicitud/<int:solicitud_id>/cancelar/', views.cancelar_solicitud, name='cancelar_solicitud'),
    path('solicitud/<int:solicitud_id>/completar/', views.completar_solicitud, name='completar_solicitud'),
]
