from django.urls import path
from .views import painel_setor
from .views import add_setor
from .views import list_setor
from .views import update_setor

#from .views import ListaGrupo
#from .views import DetailGrupo
#from .views import CreateGrupo
#from .views import UpdateGrupo
#from .views import DeleteGrupo
#from .views import ListaSetor, DetailSetor, CreateSetor, UpdateSetor


urlpatterns = [
    path('painel_setor/', painel_setor, name="painel_setor"),
    path('list_setor/', list_setor, name="list_setor"),
    path('add_setor/', add_setor, name="add_setor"),
    path('update_setor/<int:id>/', update_setor, name="update_setor"),

    #path('grupo_list', ListaGrupo.as_view(), name='grupo_list_cbv'),
    #path('grupo_detail/<int:pk>/', DetailGrupo.as_view(), name='grupo_detail_cbv'),
    #path('grupo_create', CreateGrupo.as_view(), name='grupo_create_cbv'),
    #path('grupo_update/<int:pk>/', UpdateGrupo.as_view(), name='grupo_update_cbv'),
    #path('grupo_delete/<int:pk>/', DeleteGrupo.as_view(), name='grupo_delete_cbv'),
    #path('setor_list', ListaSetor.as_view(), name='setor_list_cbv'),
    #path('setor_detail/<int:pk>/', DetailSetor.as_view(), name='setor_detail_cbv'),
    #path('setor_create', CreateSetor.as_view(), name='setor_create_cbv'),
    #path('setor_update/<int:pk>/', UpdateSetor.as_view(), name='setor_update_cbv'),
]