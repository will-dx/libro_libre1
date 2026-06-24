from django.contrib import admin
from .models import Mensaje


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ['remitente', 'solicitud', 'contenido', 'fecha']
    search_fields = ['remitente__username', 'contenido']
