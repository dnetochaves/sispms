from django.urls import path
from .views import painel_colaborador
from .views import a4
from .views import add_colaborador
from .views import list_colaborador
from .views import update_colaborador
from .views import tags_colaborador
from .views import list_tags
from .views import update_tags


urlpatterns = [
    path('painel_colaborador/', painel_colaborador, name="painel_colaborador"),
    path('a4/', a4, name="a4"),
    path('add_colaborador/', add_colaborador, name="add_colaborador"),
    path('list_colaborador/', list_colaborador, name="list_colaborador"),
    path('update_colaborador/<int:id>/', update_colaborador, name="update_colaborador"),
    path('tags_colaborador/', tags_colaborador, name="tags_colaborador"),
    path('list_tags/', list_tags, name="list_tags"),
    path('update_tags/<int:id>/', update_tags, name="update_tags"),
]