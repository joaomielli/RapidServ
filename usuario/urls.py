from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('listar_servicos/', views.listar_servicos, name='listar_servicos'),
    path('home/', views.home, name='home'),
    path('criar_servico/', views.criar_servico, name='criar_servico'),
    path('perfil/', views.perfil, name='perfil'),
    
]