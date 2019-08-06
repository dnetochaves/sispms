from django.urls import path
from .views import painel_colaborador


urlpatterns = [
    path('painel_colaborador/', painel_colaborador, name="painel_colaborador"),
]