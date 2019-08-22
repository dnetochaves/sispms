from django.urls import path
from .views import painel_colaborador
from .views import a4
from .views import add_colaborador
from .views import list_colaborador
from .views import update_colaborador
from .views import tags_colaborador
from .views import add_colaborador_remanejamento
from .views import update_colaborador_remanejamento

from .views import list_tags
from .views import update_tags

# from .views import ListaColaborador, DetailColaborador, CreateColaborador, UpdateColaborador, DeleteColaborador
# from .views import ListaTags, DetailTag, CreateTag, UpdateTag


urlpatterns = [
    path('painel_colaborador/', painel_colaborador, name="painel_colaborador"),
    path('a4/', a4, name="a4"),

    path('add_colaborador/', add_colaborador, name="add_colaborador"),
    path('add_colaborador_remanejamento/', add_colaborador_remanejamento, name="add_colaborador_remanejamento"),
    path('list_colaborador/', list_colaborador, name="list_colaborador"),
    path('update_colaborador/<int:id>/', update_colaborador, name="update_colaborador"),
    path('update_colaborador_remanejamento/<int:id>/', update_colaborador_remanejamento,
         name="update_colaborador_remanejamento"),

    path('tags_colaborador/', tags_colaborador, name="tags_colaborador"),
    path('list_tags/', list_tags, name="list_tags"),
    path('update_tags/<int:id>/', update_tags, name="update_tags"),

    # path('colaborador_list', ListaColaborador.as_view(), name='colaborador_list_cbv'),
    # path('colaborador_detail/<int:pk>/', DetailColaborador.as_view(), name='colaborador_detail_cbv'),
    # path('colaborador_create', CreateColaborador.as_view(), name='colaborador_create_cbv'),
    # path('colaborador_update/<int:pk>/', UpdateColaborador.as_view(), name='colaborador_update_cbv'),
    # path('colaborador_delete/<int:pk>/', DeleteColaborador.as_view(), name='colaborador_delete_cbv'),
    # path('tag_list', ListaTags.as_view(), name='tag_list_cbv'),
    # path('tag_detail/<int:pk>/', DetailTag.as_view(), name='tag_detail_cbv'),
    # path('tag_create', CreateTag.as_view(), name='tag_create_cbv'),
    # path('tag_update/<int:pk>/', UpdateTag.as_view(), name='tag_update_cbv'),
]