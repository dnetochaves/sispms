from django.urls import path
from .views import painel_colaborador
from .views import a4
from .views import add_colaborador


urlpatterns = [
    path('painel_colaborador/', painel_colaborador, name="painel_colaborador"),
    path('a4/', a4, name="a4"),
    path('add_colaborador/', add_colaborador, name="add_colaborador"),
]