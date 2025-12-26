from django.contrib import admin
from .models import SiteInfo, Atleta

from .models import Tarefa


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
	list_display = ('titulo_site', 'autor_projeto', 'email_contato')


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'idade', 'posicao', 'nascimento')
	search_fields = ('nome', 'posicao')


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'status', 'criado_em')
	list_filter = ('status', 'criado_em')
	search_fields = ('titulo', 'descricao')
