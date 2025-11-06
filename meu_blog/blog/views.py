from django.shortcuts import render

# --- Dicionários de Dados ---

# Informações do Site e Autores (para Sobre e Footer)
SITE_INFO = {
    "titulo_site": "Arsenal dos Sonhos FC",
    "autor_projeto": "Gemini - IA",
    "email_contato": "contato@arsenaldossonhos.com.br",
    "ano_copyright": "2024",
    "descricao_site": "Site oficial dedicado à divulgação e ao histórico do Arsenal dos Sonhos Futebol Clube, a equipe que está reescrevendo a história do futebol.",
}

# Dados dos 11 Atletas (para Equipe/Elenco)
# Observação: Usamos URLs de placeholder para simular fotos.
ELENCO_DATA = [
    {"nome": "Ricardo 'Falcão'", "idade": 30, "posicao": "Goleiro", "nascimento": "Porto Alegre, RS", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=FALCÃO"},
    {"nome": "Marcos 'Muro'", "idade": 28, "posicao": "Zagueiro", "nascimento": "São Paulo, SP", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=MURO"},
    {"nome": "Leo 'Relâmpago'", "idade": 24, "posicao": "Zagueiro", "nascimento": "Salvador, BA", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=RELÂMPAGO"},
    {"nome": "Thiago 'Coruja'", "idade": 32, "posicao": "Lateral Direito", "nascimento": "Curitiba, PR", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=CORUJA"},
    {"nome": "Bruno 'Vulcão'", "idade": 26, "posicao": "Lateral Esquerdo", "nascimento": "Rio de Janeiro, RJ", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=VULCÃO"},
    {"nome": "Pedro 'Motor'", "idade": 21, "posicao": "Volante", "nascimento": "Belo Horizonte, MG", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=MOTOR"},
    {"nome": "André 'Maestro'", "idade": 29, "posicao": "Meio-Campista", "nascimento": "Recife, PE", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=MAESTRO"},
    {"nome": "Lucas 'Flecha'", "idade": 25, "posicao": "Meia Atacante", "nascimento": "Fortaleza, CE", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=FLECHA"},
    {"nome": "Gabriel 'Gênio'", "idade": 23, "posicao": "Ponta Direita", "nascimento": "Goiânia, GO", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=GÊNIO"},
    {"nome": "João 'Artilheiro'", "idade": 27, "posicao": "Centroavante", "nascimento": "Manaus, AM", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=ARTILHEIRO"},
    {"nome": "Rafa 'Magia'", "idade": 22, "posicao": "Ponta Esquerda", "nascimento": "Brasília, DF", "foto_url": "https://placehold.co/400x400/1e293b/ffffff?text=MAGIA"},
]

# --- Funções de View ---

def home(request):
    """Renderiza a página inicial."""
    context = {
        'site_info': SITE_INFO, # Passa info para uso no template, se necessário
        'page_title': "Início",
    }
    return render(request, 'index.html', context)

def equipe(request):
    """Renderiza a página da equipe/elenco."""
    context = {
        'site_info': SITE_INFO,
        'elenco': ELENCO_DATA, # Passa a lista de atletas
        'page_title': "Equipe",
    }
    return render(request, 'equipe.html', context)

def sobre(request):
    """Renderiza a página sobre o site."""
    context = {
        'site_info': SITE_INFO, # Passa as informações do site e autores
        'page_title': "Sobre",
    }
    return render(request, 'sobre.html', context)