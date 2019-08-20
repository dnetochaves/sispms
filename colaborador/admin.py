from django.contrib import admin
from .models import Colaborador
from .models import Tags
from .models import HistoricoRemanejamento

# Register your models here.
admin.site.register(Colaborador)
admin.site.register(Tags)
admin.site.register(HistoricoRemanejamento)