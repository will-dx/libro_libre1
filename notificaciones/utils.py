from .models import Notificacion


def crear_notificacion(usuario, tipo, mensaje, enlace=''):
    Notificacion.objects.create(
        usuario=usuario,
        tipo=tipo,
        mensaje=mensaje,
        enlace=enlace,
    )
