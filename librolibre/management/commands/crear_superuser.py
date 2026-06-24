from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config


class Command(BaseCommand):
    help = 'Crea el superusuario inicial si no existe'

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            username = config('SUPERUSER_USERNAME', default='admin')
            email = config('SUPERUSER_EMAIL', default='admin@librolibre.com')
            password = config('SUPERUSER_PASSWORD', default='admin123')
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            self.stdout.write(self.style.SUCCESS(f'Superusuario creado: {username}'))
        else:
            self.stdout.write('Ya existe un superusuario.')
