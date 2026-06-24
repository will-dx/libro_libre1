from django.urls import path
from . import views

urlpatterns = [
    path('<int:solicitud_id>/', views.chat, name='chat'),
]
