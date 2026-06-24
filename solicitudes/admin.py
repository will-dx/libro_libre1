from django.contrib import admin
from .models import Solicitud


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['libro', 'solicitante', 'propietario', 'estado', 'fecha']
    list_filter = ['estado']
    search_fields = ['libro__titulo', 'solicitante__username', 'propietario__username']
