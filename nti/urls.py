from django.urls import path
from .views import index, equipamentos, add_equipamento, tags, add_tags, search_equipamento, search, remanejar_equipamento, finalizar_remanejar_equipamento, hitorico

urlpatterns = [
    path('', index, name="nti"),
    path('equipamentos/', equipamentos, name="equipamentos"),
    path('add_equipamento', add_equipamento, name="add_equipamento"),
    path('search_equipamento/<str:param>/',
         search_equipamento, name="search_equipamento"),
    path('remanejar_equipamento/<int:id>/',
         remanejar_equipamento, name="remanejar_equipamento"),
    path('finalizar_remanejar_equipamento/<int:id>/',
         finalizar_remanejar_equipamento, name="finalizar_remanejar_equipamento"),
    path('hitorico/<int:id>/',
         hitorico, name="hitorico"),
    path('search/', search, name="search"),
    path('tags', tags, name="tags"),
    path('add_tags', add_tags, name="add_tags"),
]
