from django.contrib import admin
from .models import Colaborador
from .models import Tags
from .models import HistoricoRemanejamento, Cargo, Empresa

# Register your models here.
admin.site.register(Colaborador)
admin.site.register(Tags)
admin.site.register(HistoricoRemanejamento)
admin.site.register(Cargo)
admin.site.register(Empresa)