from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth ,messages
from login.models import PerfilAluno
from login.models import Pessoa
from login.models import materia
import random

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        numero = request.POST['telefone']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        sexo = request.POST['sexo']
        aulas = ""
        usuario = request.POST['usuario']
        aniversario = request.POST['nasc']
        try:
            fotos = request.FILES['foto']
        except :
            fotos = '/media/static/imagens/user.png'



    



        if not username.strip():
            print('O campo Username não pode ficar em branco')
            messages.error(request, 'O campo Username não pode ficar em branco')
            
            return redirect('cadastro')
        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco')
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not sobrenome.strip():
            messages.error(request, 'O campo sobrenome não pode ficar em branco')
            print('O campo sobrenome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O campo email não pode ficar em branco')
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais')
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            messages.error(request, 'Email já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=username).exists():
            print('Usuário já cadastrado')
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')


        
        user = User.objects.create_user(username=username, email=email, password=senha,first_name=nome, last_name =sobrenome)  
        user.save() 
        user = auth.authenticate(request, username=username, password=senha)
        auth.login(request, user)

        profile = PerfilAluno.objects.create(telefone=numero,estado=estado,cidade=cidade,sexo=sexo,aulas=aulas,user_id = request.user.id,aniversario=aniversario,foto=fotos,usuario=usuario,quantidade=0)     
        profile.save()
        
        print('Usuário cadastrado com sucesso')

        pessoa = Pessoa.objects.create(nome=nome,email=email,username=username,telefone=numero,senha=senha)
        pessoa.save()

        
        return redirect('dashboard')
    else:
        return render(request,'cadastro.html')


def login(request):
    if request.method == 'POST':
        usuario =  request.POST['usuario']
        senha = request.POST["senha"]
        if usuario == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            print(usuario, senha)
            return render(request,'login.html')
        if User.objects.filter(email=usuario).exists():
            nome = User.objects.filter(email=usuario).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
            print(nome)
        user = auth.authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth.login(request, user)
            print('Login realizado com sucesso')
            
            return redirect('dashboard')

        return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')
    
def perfil(request):
    
    if request.user.is_authenticated:
        profiles = PerfilAluno.objects.get(user=request.user.id)
        
        if profiles.usuario == "1":
            return render(request,'user_aluno.html')
        profiles = PerfilAluno.objects.get(user=request.user.id)
        materias = materia.objects.filter(professor=request.user.id)

        dados={
        'profiles' : profiles,
        'materia' : materias,
        
        }
   
        return render(request,'user.html',dados)
    else:
        return redirect('login')
    

def alterarsenha(request):
    if request.method == 'POST':
        print("teste")
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            print("entrou")
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, "Perfil.html")
        else:
            print("não entrou")
            return redirect("index")
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form':form,
        }
        return render(request, "alterarsenha.html",context)

def alterardado(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        url = request.POST['url']
        telefone = request.POST['telefone']
        print(nome,sobrenome,email,url,telefone)
        profiles = Profile.objects.get(user=request.user.id)

        profiles.urltrade = url
        profiles.numero = telefone
        profiles.save()

        request.user.first_name = nome
        request.user.last_name = sobrenome
        request.user.email = email

        request.user.save()


        


    return redirect('perfil')

def ativar(request):
    return render(request,'ativarConta.html')

def esquecisenha(request):
    return render(request,'esquecisenha.html')

    
def resetsenha(request):
    return render(request,'esquecisenha.html')


