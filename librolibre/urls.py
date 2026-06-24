from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    query = request.GET.get('q', '')
    filtro_tipo = request.GET.get('tipo', '')
    filtro_disp = request.GET.get('disponibilidad', '')
    try:
        from libros.models import Book
        libros = Book.objects.all()
        if query:
            from django.db.models import Q
            libros = libros.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
        if filtro_tipo:
            libros = libros.filter(tipo=filtro_tipo)
        if filtro_disp:
            libros = libros.filter(estado=filtro_disp)
    except Exception:
        libros = []
    return render(request, 'home.html', {
        'libros': libros,
        'query': query,
        'filtro_tipo': filtro_tipo,
        'filtro_disp': filtro_disp,
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('libros/', include('libros.urls')),
    path('solicitudes/', include('solicitudes.urls')),
    path('mensajes/', include('mensajes.urls')),
    path('encuentros/', include('encuentros.urls')),
]

if not settings.USE_SUPABASE:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
