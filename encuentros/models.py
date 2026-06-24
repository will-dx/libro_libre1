from django.db import models
from solicitudes.models import Solicitud


class PuntoEncuentro(models.Model):
    solicitud = models.OneToOneField(Solicitud, on_delete=models.CASCADE, related_name='punto_encuentro')
    latitud = models.FloatField()
    longitud = models.FloatField()
    direccion = models.CharField(max_length=300, blank=True)
    fecha_entrega = models.DateField()
    hora_entrega = models.TimeField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Encuentro: {self.direccion} ({self.fecha_entrega})'
