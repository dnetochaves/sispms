from django.urls import path
from .views import painel_setor
from .views import add_setor
from .views import list_setor
from .views import update_setor


urlpatterns = [
    path('painel_setor/', painel_setor, name="painel_setor"),
    path('list_setor/', list_setor, name="list_setor"),
    path('add_setor/', add_setor, name="add_setor"),
    path('update_setor/<int:id>/', update_setor, name="update_setor"),
]