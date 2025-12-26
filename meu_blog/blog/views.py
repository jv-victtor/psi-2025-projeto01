from django.shortcuts import render, redirect
from .models import SiteInfo, Atleta
from .forms import AtletaForm
from django.shortcuts import get_object_or_404


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

    if request.method == 'POST':
        form = AtletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = AtletaForm()

    elenco = Atleta.objects.all()
    context = {
        'site_info': site_info,
        'elenco': elenco,
        'page_title': "Equipe",
        'form': form,
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


def editar_atleta(request, pk):
    """Editar um atleta existente via AtletaForm."""
    atleta = get_object_or_404(Atleta, pk=pk)
    if request.method == 'POST':
        form = AtletaForm(request.POST, instance=atleta)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = AtletaForm(instance=atleta)

    return render(request, 'atleta_form.html', {'form': form, 'atleta': atleta, 'page_title': 'Editar Atleta', 'site_info': _get_site_info()})


def deletar_atleta(request, pk):
    """Confirma e deleta um atleta."""
    atleta = get_object_or_404(Atleta, pk=pk)
    if request.method == 'POST':
        atleta.delete()
        return redirect('equipe')

    return render(request, 'atleta_confirm_delete.html', {'atleta': atleta, 'site_info': _get_site_info(), 'page_title': 'Deletar Atleta'})