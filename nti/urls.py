from django.urls import path
from .views import index, equipamentos, add_equipamento,tags, add_tags, search_equipamento

urlpatterns = [
    path('', index, name="nti"),
    path('equipamentos/', equipamentos, name="equipamentos"),
    path('add_equipamento', add_equipamento, name="add_equipamento"),
    path('search_equipamento/<str:param>/', search_equipamento, name="search_equipamento"),
    path('tags', tags, name="tags"),
    path('add_tags', add_tags, name="add_tags"),
]
