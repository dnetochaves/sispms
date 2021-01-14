from django.urls import path
from .views import painel_colaborador
from .views import a4
from .views import add_colaborador
from .views import list_colaborador
from .views import list_setor_colaborador
from .views import list_colaborador_por_setor
from .views import update_colaborador
from .views import tags_colaborador
from .views import add_colaborador_remanejamento
from .views import update_colaborador_remanejamento
from .views import list_historico_remanejamento
from .views import carta_encaminhamento_colaborador
from .views import observacao_colaborador
from .views import list_tags
from .views import update_tags
from .views import info_tags
from .views import list_historico


# Refatoração
from .views import colaborador, new_colaborador, search_colaborador, edit_colaborador, remanejar, finalizar_remanejar, carta_encaminhamento, colaborador_setor, setor_colaborador


urlpatterns = [
    path('painel_colaborador/', painel_colaborador, name="painel_colaborador"),
    path('a4/', a4, name="a4"),

    path('add_colaborador/', add_colaborador, name="add_colaborador"),
    path('add_colaborador_remanejamento/', add_colaborador_remanejamento,
         name="add_colaborador_remanejamento"),
    path('list_colaborador/', list_colaborador, name="list_colaborador"),
    path('list_colaborador_por_setor/<int:id>/',
         list_colaborador_por_setor, name="list_colaborador_por_setor"),
    path('list_setor_colaborador/', list_setor_colaborador,
         name="list_setor_colaborador"),
    path('list_historico_remanejamento/<int:id>/',
         list_historico_remanejamento, name="list_historico_remanejamento"),
    path('update_colaborador/<int:id>/',
         update_colaborador, name="update_colaborador"),
    path('carta_encaminhamento_colaborador/<int:id>/', carta_encaminhamento_colaborador,
         name="carta_encaminhamento_colaborador"),
    path('update_colaborador_remanejamento/<int:id>/', update_colaborador_remanejamento,
         name="update_colaborador_remanejamento"),
    path('observacao_colaborador/<int:id>/', observacao_colaborador,
         name="observacao_colaborador"),

    path('tags_colaborador/', tags_colaborador, name="tags_colaborador"),
    path('list_tags/', list_tags, name="list_tags"),
    path('info_tags/<int:id>/', info_tags, name="info_tags"),
    path('update_tags/<int:id>/', update_tags, name="update_tags"),
    path('list_historico/', list_historico, name="list_historico"),

    # Refatoração
    path('colaborador/', colaborador, name="colaborador"),
    path('new_colaborador/', new_colaborador, name="new_colaborador"),
    path('search_colaborador/', search_colaborador, name="search_colaborador"),
    path('edit_colaborador/<int:id>/', edit_colaborador, name="edit_colaborador"),
    path('remanejar/<int:id_colaborador>/', remanejar, name="remanejar"),
    path('finalizar_remanejar/<int:id_setor_atu>/',
         finalizar_remanejar, name="finalizar_remanejar"),
    path('carta_encaminhamento/<int:id>/',
         carta_encaminhamento, name="carta_encaminhamento"),
    path('colaborador_setor/<int:id>/',
         colaborador_setor, name="colaborador_setor"),
    path('setor_colaborador/',
         setor_colaborador, name="setor_colaborador"),
]
