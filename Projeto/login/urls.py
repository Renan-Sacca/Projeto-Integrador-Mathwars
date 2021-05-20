from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('perfil', views.perfil, name='perfil'),
    path('alterarsenha', views.alterarsenha, name='alterarsenha'),
    path('alterardado', views.alterardado, name='alterardado'),
    path('ativar', views.ativar, name='ativar'),
    path('esquecisenha', views.esquecisenha, name='esquecisenha'),
    path('resetsenha', views.resetsenha, name='resetsenha'),
]