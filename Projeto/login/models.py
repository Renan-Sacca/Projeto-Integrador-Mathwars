from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    senha = models.CharField(max_length=50)

class materia(models.Model):
    nome = models.CharField(max_length=200)
    professor = models.IntegerField()
    alunos =  models.CharField(max_length=100)

class exercicioss(models.Model):
    nome = models.CharField(max_length=50)
    enunciado = models.CharField(max_length=99999)
    resposta = models.CharField(max_length=99999)
    materia = models.IntegerField()

class exerciciossr(models.Model):
    nome = models.CharField(max_length=50)
    enunciado = models.CharField(max_length=99999)
    resposta = models.CharField(max_length=99999)
    materia = models.IntegerField()

class estado(models.Model):
    nome = models.CharField(max_length=50)
    

class cidades(models.Model):
    nome = models.CharField(max_length=50)
    user = models.ForeignKey(estado, on_delete=models.CASCADE)

class PerfilAluno(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    sexo =  models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    usuario = models.CharField(max_length=2)
    aulas = models.CharField(max_length=200)
    aniversario = models.DateField()
    turmas = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    quantidade = models.IntegerField()

class exercicios(models.Model):
    nome = models.CharField(max_length=50)
    enunciado = models.CharField(max_length=1000)
    resposta = models.CharField(max_length=1000)
    
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)






