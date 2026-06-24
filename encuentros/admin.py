from django.contrib import admin
from .models import PuntoEncuentro


@admin.register(PuntoEncuentro)
class PuntoEncuentroAdmin(admin.ModelAdmin):
    list_display = ['solicitud', 'direccion', 'fecha_entrega', 'hora_entrega']
    search_fields = ['direccion', 'solicitud__libro__titulo']
