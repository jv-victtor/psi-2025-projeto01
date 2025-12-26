from django.shortcuts import render
from .models import SiteInfo, Atleta


def _get_site_info():
    """Retorna a instância de SiteInfo (primeira) ou None se não existir."""
    return SiteInfo.objects.first()


def home(request):
    """Renderiza a página inicial usando dados do model SiteInfo."""
    site_info = _get_site_info()
    context = {
        'site_info': site_info,
        'page_title': "Início",
    }
    return render(request, 'index.html', context)


def equipe(request):
    """Renderiza a página da equipe/elenco lendo os atletas do model Atleta."""
    site_info = _get_site_info()
    elenco = Atleta.objects.all()
    context = {
        'site_info': site_info,
        'elenco': elenco,
        'page_title': "Equipe",
    }
    return render(request, 'equipe.html', context)


def sobre(request):
    """Renderiza a página sobre o site usando SiteInfo."""
    site_info = _get_site_info()
    context = {
        'site_info': site_info,
        'page_title': "Sobre",
    }
    return render(request, 'sobre.html', context)