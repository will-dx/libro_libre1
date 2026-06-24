from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notificacion


@login_required
def listar(request):
    notificaciones = request.user.notificaciones.all()
    return render(request, 'notificaciones/listar.html', {
        'notificaciones': notificaciones,
    })


@login_required
def marcar_leido(request, notificacion_id):
    notif = get_object_or_404(Notificacion, id=notificacion_id, usuario=request.user)
    notif.leido = True
    notif.save()
    return JsonResponse({'ok': True})


@login_required
def marcar_todo_leido(request):
    request.user.notificaciones.filter(leido=False).update(leido=True)
    return JsonResponse({'ok': True})
