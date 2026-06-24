from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'tipo', 'estado', 'owner', 'fecha_publicacion']
    list_filter = ['tipo', 'estado']
    search_fields = ['titulo', 'autor', 'owner__username']
