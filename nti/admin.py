from django.contrib import admin
from .models import Equipamento, Tags, Historico

# Register your models here.
admin.site.register(Equipamento)
admin.site.register(Tags)
admin.site.register(Historico)
