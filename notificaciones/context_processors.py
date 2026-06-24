from .models import Notificacion


def notificaciones_processor(request):
    if request.user.is_authenticated:
        no_leidas = Notificacion.objects.filter(usuario=request.user, leido=False).count()
        ultimas = Notificacion.objects.filter(usuario=request.user)[:5]
        return {'notif_no_leidas': no_leidas, 'notif_ultimas': ultimas}
    return {'notif_no_leidas': 0, 'notif_ultimas': []}
