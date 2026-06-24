from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='notificaciones'),
    path('<int:notificacion_id>/leido/', views.marcar_leido, name='marcar_leido'),
    path('todo-leido/', views.marcar_todo_leido, name='marcar_todo_leido'),
]
