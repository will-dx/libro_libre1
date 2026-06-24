from django.db import models
from django.contrib.auth.models import User
from solicitudes.models import Solicitud


class Mensaje(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, related_name='mensajes')
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return f'{self.remitente.username}: {self.contenido[:50]}'
