from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Solicitud
from libros.models import Book


@login_required
def solicitar_libro(request, libro_id):
    libro = get_object_or_404(Book, id=libro_id)
    if libro.owner == request.user:
        messages.error(request, 'No puedes solicitar tu propio libro.')
        return redirect('detalle_libro', libro_id=libro.id)
    if libro.estado != 'disponible':
        messages.error(request, 'Este libro no está disponible.')
        return redirect('detalle_libro', libro_id=libro.id)
    if Solicitud.objects.filter(solicitante=request.user, libro=libro, estado='pendiente').exists():
        messages.error(request, 'Ya tienes una solicitud pendiente para este libro.')
        return redirect('detalle_libro', libro_id=libro.id)

    Solicitud.objects.create(
        solicitante=request.user,
        libro=libro,
        propietario=libro.owner,
    )
    messages.success(request, 'Solicitud enviada. Espera la respuesta del propietario.')
    return redirect('detalle_libro', libro_id=libro.id)


@login_required
def aceptar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id, propietario=request.user, estado='pendiente')
    solicitud.estado = 'aceptada'
    solicitud.save()
    messages.success(request, 'Solicitud aceptada. El chat está habilitado.')
    return redirect('ver_solicitud', solicitud_id=solicitud.id)


@login_required
def rechazar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id, propietario=request.user, estado='pendiente')
    solicitud.estado = 'rechazada'
    solicitud.save()
    messages.success(request, 'Solicitud rechazada.')
    return redirect('perfil')


@login_required
def cancelar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id, solicitante=request.user, estado='pendiente')
    solicitud.estado = 'cancelada'
    solicitud.save()
    messages.success(request, 'Solicitud cancelada.')
    return redirect('perfil')


@login_required
def completar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id, propietario=request.user, estado='aceptada')
    solicitud.estado = 'completada'
    solicitud.save()
    solicitud.libro.estado = 'no_disponible'
    solicitud.libro.save()
    messages.success(request, 'Solicitud marcada como completada.')
    return redirect('perfil')


@login_required
def ver_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.user not in [solicitud.solicitante, solicitud.propietario]:
        messages.error(request, 'No tienes acceso a esta solicitud.')
        return redirect('home')
    return render(request, 'solicitudes/detalle.html', {'solicitud': solicitud})
