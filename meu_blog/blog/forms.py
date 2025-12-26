from django import forms
from .models import Atleta


class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ['nome', 'idade', 'posicao', 'nascimento', 'foto_url']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'idade': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'posicao': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'nascimento': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'foto_url': forms.URLInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
        }
