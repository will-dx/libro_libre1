from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from solicitudes.models import Solicitud


@login_required
def chat(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.user not in [solicitud.solicitante, solicitud.propietario]:
        messages.error(request, 'No tienes acceso a este chat.')
        return redirect('home')
    if solicitud.estado != 'aceptada' and solicitud.estado != 'completada':
        messages.error(request, 'El chat se habilita cuando la solicitud es aceptada.')
        return redirect('ver_solicitud', solicitud_id=solicitud.id)

    if request.method == 'POST':
        contenido = request.POST.get('contenido', '').strip()
        if contenido:
            Mensaje.objects.create(
                solicitud=solicitud,
                remitente=request.user,
                contenido=contenido,
            )
        return redirect('chat', solicitud_id=solicitud.id)

    mensajes = solicitud.mensajes.all()
    otro_usuario = solicitud.propietario if solicitud.solicitante == request.user else solicitud.solicitante
    return render(request, 'mensajes/chat.html', {
        'solicitud': solicitud,
        'mensajes': mensajes,
        'otro_usuario': otro_usuario,
    })
