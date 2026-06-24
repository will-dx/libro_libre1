from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)


class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'is_active', 'date_joined']
    list_filter = ['is_active', 'is_staff']
    search_fields = ['username', 'email', 'first_name']


admin.site.register(User, UsuarioAdmin)
