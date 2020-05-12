from django.urls import path
from .views import painel_setor
from .views import add_setor
from .views import list_setor
from .views import update_setor
from .views import list_grupo
from .views import add_grupo
from .views import update_grupo
from .views import teste
from .views import painel_demandas
from .views import add_item
from .views import list_item
from .views import update_item
from .views import list_tag
from .views import add_tag
from .views import info_tag
from .views import info_status
from .views import update_tag
from .views import list_demandas
from .views import list_status
from .views import add_status
from .views import add_demanda
from .views import update_demanda
from .views import list_grupo_setor
from .views import filtrar_demanda_setor

# from .views import ListaGrupo
# from .views import DetailGrupo
# from .views import CreateGrupo
# from .views import UpdateGrupo
# from .views import DeleteGrupo
# from .views import ListaSetor, DetailSetor, CreateSetor, UpdateSetor


urlpatterns = [
    path('painel_setor/', painel_setor, name="painel_setor"),
    path('painel_demandas/', painel_demandas, name="painel_demandas"),
    path('list_setor/', list_setor, name="list_setor"),
    path('list_grupo/', list_grupo, name="list_grupo"),
    path('add_setor/', add_setor, name="add_setor"),
    path('add_grupo/', add_grupo, name="add_grupo"),
    path('add_item/', add_item, name="add_item"),
    path('list_item/', list_item, name="list_item"),
    path('list_tag/', list_tag, name="list_tag"),
    path('add_tag/', add_tag, name="add_tag"),
    path('info_tag/<int:id>/', info_tag, name="info_tag"),
    path('info_status/<int:id>/', info_status, name="info_status"),
    path('list_demandas/', list_demandas, name="list_demandas"),
    path('list_status/', list_status, name="list_status"),
    path('add_status/', add_status, name="add_status"),
    path('add_demanda/', add_demanda, name="add_demanda"),
    path('update_demanda/<int:id>/', update_demanda, name="update_demanda"),
    path('update_tag/<int:id>/', update_tag, name="update_tag"),
    path('update_item/<int:id>/', update_item, name="update_item"),
    path('update_setor/<int:id>/', update_setor, name="update_setor"),
    path('update_grupo/<int:id>/', update_grupo, name="update_grupo"),
    path('filtrar_demanda_setor/<int:id>/', filtrar_demanda_setor, name="filtrar_demanda_setor"),
    path('list_grupo_setor/', list_grupo_setor, name="list_grupo_setor"),
    path('teste/', teste, name="teste"),

    # path('grupo_list', ListaGrupo.as_view(), name='grupo_list_cbv'),
    # path('grupo_detail/<int:pk>/', DetailGrupo.as_view(), name='grupo_detail_cbv'),
    # path('grupo_create', CreateGrupo.as_view(), name='grupo_create_cbv'),
    # path('grupo_update/<int:pk>/', UpdateGrupo.as_view(), name='grupo_update_cbv'),
    # path('grupo_delete/<int:pk>/', DeleteGrupo.as_view(), name='grupo_delete_cbv'),
    # path('setor_list', ListaSetor.as_view(), name='setor_list_cbv'),
    # path('setor_detail/<int:pk>/', DetailSetor.as_view(), name='setor_detail_cbv'),
    # path('setor_create', CreateSetor.as_view(), name='setor_create_cbv'),
    # path('setor_update/<int:pk>/', UpdateSetor.as_view(), name='setor_update_cbv'),
]
