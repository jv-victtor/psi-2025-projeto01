from django.contrib import admin
from .models import SiteInfo, Atleta


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
	list_display = ('titulo_site', 'autor_projeto', 'email_contato')


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'idade', 'posicao', 'nascimento')
	search_fields = ('nome', 'posicao')
