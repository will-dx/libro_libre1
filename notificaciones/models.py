from django.db import models
from django.contrib.auth.models import User


class Notificacion(models.Model):
    TIPO_CHOICES = [
        ('solicitud', 'Solicitud'),
        ('aceptada', 'Solicitud aceptada'),
        ('rechazada', 'Solicitud rechazada'),
        ('cancelada', 'Solicitud cancelada'),
        ('completada', 'Solicitud completada'),
        ('mensaje', 'Nuevo mensaje'),
        ('encuentro', 'Punto de encuentro'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    mensaje = models.CharField(max_length=255)
    enlace = models.CharField(max_length=255, blank=True)
    leido = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.usuario.username}: {self.mensaje[:50]}'
