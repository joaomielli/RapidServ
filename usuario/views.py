from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        usuario = User.objects.filter(username=username).first()

        if usuario:
            return HttpResponse("Já existe um usuário com esse username")
            print(f"usuario: {usuario}")

        usuario = User.objects.create_user(
            username=username, email=email, password=senha
        )
        usuario.save()

        return HttpResponse(f"Usuário:{username} cadastrado com sucesso")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        usuario = authenticate(username=username, password=senha)

        if usuario:
            login_django(request, usuario)
            return HttpResponse("autenticado")
        else:
            return HttpResponse("Email ou senha inválidos")


@login_required(login_url="/auth/login/")
def buscar_servicos(request):
    return HttpResponse("Buscar Serviços")
