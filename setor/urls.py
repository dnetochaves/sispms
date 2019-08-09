from django.urls import path
from .views import painel_setor


urlpatterns = [
    path('painel_setor/', painel_setor, name="painel_setor"),
]