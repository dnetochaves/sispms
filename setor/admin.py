from django.contrib import admin
from .models import Setor, Grupo, Item, Tags, Demandas, Status

# Register your models here.
admin.site.register(Setor)
admin.site.register(Grupo)
admin.site.register(Item)
admin.site.register(Tags)
admin.site.register(Demandas)
admin.site.register(Status)