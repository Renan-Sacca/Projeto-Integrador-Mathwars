from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth ,messages
from login.models import PerfilAluno
from login.models import Pessoa
from login.models import exercicios
from login.models import exercicioss,exerciciossr
from login.models import materia
import random
import login.views

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages

def dashboard(request):

    if request.user.is_authenticated:
        profiles = PerfilAluno.objects.get(user=request.user.id)
        
        if profiles.usuario == "1":
            turma = profiles.turmas
            turma = turma.split(",")[:-1]
            print(turma)
            if len(turma) > 0:
                exercicio = exercicioss.objects.filter(materia=int(turma[0]))
            
                dados={
                'exercicios' : exercicio,            }
            else:
                dados={}
            return render(request,'dashboard.html',dados)




        else:
            
            alunos = PerfilAluno.objects.filter(usuario=1)
            o = 0
            for aluno in alunos:
                o+=1
            dados = {
                'ativos' : o,
    
            }
            return render(request,'teacher_dashboard.html',dados)
    else:
        return redirect('login')


def propor_exercicio(request):
    perguntas = []
    respostas = []
   
    if request.user.is_authenticated:
        profiles = PerfilAluno.objects.get(user=request.user.id)
        if profiles.usuario == "1":

            return render(request,'dashboard.html')
        else:
            if request.method == 'POST':
                quantidade_questoes = request.POST['numerodequestoes']
                for i in range(1,int(quantidade_questoes)+1):
                    questao = request.POST['questao' + str(i)]
                    if request.POST['questao' + str(i) + "_e"] == '1':
                        respostarr = []
                        pergunta = request.POST['questao' + str(i)]
                        perguntas.append(pergunta)
                        quantidade_alternativas = request.POST['quantidadealternativas' + str(i)]
                        for j in range(1,int(quantidade_alternativas)+1):
                            respostar = request.POST['resposta_' + str(i) + "_" + str(j)]
            
                            respostarr.append(respostar)
                        
                        radio = request.POST['radio' + str(i)]
                        #respostarr.append(radio)
                        respostaaaaaa = [len(respostarr)]
                        for k in respostarr:
                            respostaaaaaa.append(k)
                        respostas.append(respostaaaaaa)
                        
                    else:
                        pergunta = request.POST['questao' + str(i)]
                        respostas.append("0")
                        perguntas.append(pergunta)
                
                nome = request.POST['nomedoexercicio']
                materiass = request.POST['select']
                questao = exercicioss.objects.create(nome=nome, enunciado=str(perguntas), resposta=str(respostas),materia=int(materiass))  
                questao.save() 
                questaoq = exerciciossr.objects.create(nome=nome, enunciado= "alunos=", resposta="alunos=",materia=int(materiass))  
                questaoq.save() 




                return render(request,'propor.html')
            else:
                materias = materia.objects.filter(professor=request.user.id)
                dados = {
                    'materia' : materias,
        
                }
                
                return render(request,'propor.html',dados)
    else:
        return redirect('login')



def materias(request):
    if request.user.is_authenticated:
            profiles = PerfilAluno.objects.get(user=request.user.id)
            if profiles.usuario == "1":

                return render(request,'dashboard.html')
            else:
                if request.method == 'POST':
                    nome = request.POST['materia']
                    alunos = ""
                    id = request.user.id
                    questao = materia.objects.create(nome=nome,professor=id,alunos=alunos) 
                    questao.save()




                    return redirect('dashboard')
                else:
                    return render(request,'materia.html')
    else:
        return redirect('login')


def turma(request):
    if request.user.is_authenticated:
        profiles = PerfilAluno.objects.get(user=request.user.id)
        
        if profiles.usuario == "1":
            if request.method == 'POST':
                nome = request.POST['materia']
                materiaa = materia.objects.get(id=int(nome))
                turmaa = profiles.turmas
                turmaa += nome + ","
                
                materias = materiaa.alunos
                materias +=   str(profiles.id) + ","
                materiaa.alunos = materias
                materiaa.save()
                profiles.turmas = turmaa
                profiles.save()
                

                return redirect('dashboard')
            else:
                return render(request,'entrar.html')

def responder(request):
    if request.user.is_authenticated:
        profiles = PerfilAluno.objects.get(user=request.user.id)
        
        if profiles.usuario == "1":
            profiles = PerfilAluno.objects.get(user=request.user.id)
            turma = profiles.turmas
            turma = turma.split(",")[:-1]
            materias = []
            for i in turma:
                materiaa = materia.objects.get(id=int(i))
                materias.append(materiaa)
            dados = {
                "materia": materias,
                "inicio":1,
            }

            if request.method == 'POST':
                questoes = request.POST['inicio']
                if questoes == "1":
                    profiles = PerfilAluno.objects.get(user=request.user.id)
                    questoess = request.POST['select']
                    exercicio = exercicioss.objects.filter(materia=int(questoess))
                    dados = {
                    "exercicios": exercicio,
                    "inicio":2,
                        }
                elif questoes == "2":
                    questoess = request.POST['select2']
                    id_q = questoess
                    exercicio = exercicioss.objects.get(id=int(questoess))
                    enunciados = exercicio.enunciado
                    resposta = exercicio.resposta
                    enunciados = enunciados.split(",")
                    resposta = resposta.split(",")
                    enu = []
                    res = []
                    for i in enunciados:
                        enunciadoss = i 
                        enunciadoss = enunciadoss.replace("[","")
                        enunciadoss = enunciadoss.replace("]","")
                        enunciadoss = enunciadoss.replace("'","")
                        enu.append(enunciadoss)

                    for i in resposta:
                        respostasss = i 
                        respostasss = respostasss.replace("[","")
                        respostasss = respostasss.replace("]","")
                        respostasss = respostasss.replace("'","")
                        res.append(respostasss)

                    enviar = []
                    pos = 0
                    alt = []
                    aux = True
                    i = 0
                    print(res)
                    while aux:
                        if res[i] == '0' or  res[i] == ' 0':
                            enun = [0,enu[pos], "resposta" + str(pos+1),0]
                            enviar.append(enun)
                            pos+=1
                            del(res[0])
                        else:
                            print("res 0 ", res[0])
                            
                            auxx = int(res[0])
                            auxxx= True
                            print(auxx)
                            while auxxx:
                                
                                alt.append([res[1],len(alt)+1])
                                auxx-=1
                                del(res[1])
                                
                                print(res)
                                if auxx == 0:
                                    
                                    del(res[0])
                                    
                                    auxxx = False
                                    env = [1,enu[pos], "resposta" + str(pos+1),len(alt),alt]
                                    
                                    enviar.append(env)
                                    alt = []
                                    pos+=1
                        if len(res) == 0:
                            aux = False 
                        
                        


                        


                    print(enviar)
                    print(pos)
                    dados = {
                        "perguntas": enviar,
                    "inicio":3,
                    "perguntass":pos,
                    "id_q":id_q,
                        }
                    return render(request,'responder.html',dados)
                elif questoes == "3":
                    quantidade = request.POST['perguntass']
                    id_q =  request.POST['id_q']
                   
                    resposta_f = []
                    for i in range(1,int(quantidade)+1):
                        resposta_q = request.POST['resposta' + str(i)]
                        resposta_f.append(resposta_q)
                    
                    aluno_e = exerciciossr.objects.get(id=int(id_q))
                    enunci = aluno_e.enunciado
                    respos = aluno_e.resposta
                    aluno_e.enunciado = enunci + str(request.user.id) + ","
                    aluno_e.resposta = respos + str(resposta_f) +","
                    aluno_e.save()
                return render(request,'responder.html',dados)
                    
                

                
            else:

                return render(request,'responder.html',dados)


            