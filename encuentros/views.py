from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PuntoEncuentro
from solicitudes.models import Solicitud


@login_required
def crear_encuentro(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id, propietario=request.user, estado='aceptada')
    if hasattr(solicitud, 'punto_encuentro'):
        messages.error(request, 'Ya existe un punto de encuentro para esta solicitud.')
        return redirect('ver_solicitud', solicitud_id=solicitud.id)

    if request.method == 'POST':
        PuntoEncuentro.objects.create(
            solicitud=solicitud,
            latitud=request.POST.get('latitud'),
            longitud=request.POST.get('longitud'),
            direccion=request.POST.get('direccion', ''),
            fecha_entrega=request.POST.get('fecha_entrega'),
            hora_entrega=request.POST.get('hora_entrega'),
        )
        messages.success(request, 'Punto de encuentro creado.')
        return redirect('ver_encuentro', solicitud_id=solicitud.id)

    return render(request, 'encuentros/crear.html', {'solicitud': solicitud})


@login_required
def ver_encuentro(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.user not in [solicitud.solicitante, solicitud.propietario]:
        messages.error(request, 'No tienes acceso a este punto de encuentro.')
        return redirect('home')
    encuentro = get_object_or_404(PuntoEncuentro, solicitud=solicitud)
    return render(request, 'encuentros/ver.html', {
        'encuentro': encuentro,
        'solicitud': solicitud,
    })
