from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('propor', views.propor_exercicio, name='propor_exercicio'),
    path('materia', views.materias, name='materia'),
    path('turma', views.turma, name='turma'),
    path('responder', views.responder, name='responder'),

    
    

]