from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm


def detalle_libro(request, libro_id):
    libro = get_object_or_404(Book, id=libro_id)
    return render(request, 'libros/detalle.html', {'libro': libro})


@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.owner = request.user
            try:
                libro.save()
                messages.success(request, 'Libro publicado correctamente.')
                return redirect('detalle_libro', libro_id=libro.id)
            except Exception:
                messages.error(request, 'Error al subir la imagen. Intenta de nuevo.')
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = BookForm()
    return render(request, 'libros/crear.html', {'form': form})


@login_required
def editar_libro(request, libro_id):
    libro = get_object_or_404(Book, id=libro_id, owner=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado.')
            return redirect('detalle_libro', libro_id=libro.id)
    else:
        form = BookForm(instance=libro)
    return render(request, 'libros/crear.html', {'form': form, 'editando': True})


@login_required
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Book, id=libro_id, owner=request.user)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado.')
        return redirect('perfil')
    return render(request, 'libros/confirmar_eliminar.html', {'libro': libro})
