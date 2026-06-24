from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    TIPO_CHOICES = [
        ('prestamo', 'Préstamo'),
        ('donacion', 'Donación'),
    ]
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('no_disponible', 'No disponible'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    imagen = models.ImageField(upload_to='libros/')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    @property
    def imagen_url(self):
        try:
            return self.imagen.url
        except Exception:
            return ''
