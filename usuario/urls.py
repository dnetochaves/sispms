from django.urls import path
from .views import hello
from .views import list_usuario
from .views import new_usuario
from .views import update_usuario
from .views import delete_usuario
from .views import perfil
from .views import painel_configuracao
from .views import add_nota
from .views import update_nota

urlpatterns = [
    path('hello/', hello, name="hello"),
    path('perfil/', perfil, name="perfil"),
    path('list_usuario/', list_usuario, name="list_usuario"),
    path('new_usuario/', new_usuario, name="new_usuario"),
    path('add_nota/', add_nota, name="add_nota"),
    path('update_nota/<int:id>/', update_nota, name="update_nota"),
    path('update_usuario/<int:id>/', update_usuario, name="update_usuario"),
    path('delete_usuario/<int:id>/', delete_usuario, name="delete_usuario"),
    path('painel_configuracao', painel_configuracao, name="painel_configuracao"),
]
