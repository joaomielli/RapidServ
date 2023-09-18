from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


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

        usuario = User.objects.create_user(username=username, email=email, password=senha)
        usuario.save()

        return HttpResponse(f'Usuário:{username} cadastrado com sucesso')


def login(request):
    return render(request, "login.html")
