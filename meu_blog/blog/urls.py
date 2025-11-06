from django.urls import path
from . import views

# Definição das rotas do projeto
urlpatterns = [
    # Rota para a página inicial (Início)
    path('', views.home, name='home'),
    
    # Rota para a página da equipe/elenco
    path('equipe/', views.equipe, name='equipe'),
    
    # Rota para a página sobre o site
    path('sobre/', views.sobre, name='sobre'),
]