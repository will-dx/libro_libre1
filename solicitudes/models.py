from django.db import models
from django.contrib.auth.models import User
from libros.models import Book


class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes_realizadas')
    libro = models.ForeignKey(Book, on_delete=models.CASCADE)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes_recibidas')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.solicitante.username} → {self.libro.titulo} ({self.estado})'


