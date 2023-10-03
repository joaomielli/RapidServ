from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .forms import ServicoForm
from .models import Servico


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        usuario = User.objects.filter(username=username).first()

        if usuario:
            return HttpResponse("Já existe um usuário com esse username")

        usuario = User.objects.create_user(
            username=username, email=email, password=senha
        )
        usuario.save()

        return render(request, 'home.html', {'exibir_popup': True})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        usuario = authenticate(username=username, password=senha)

        if usuario:
            login_django(request, usuario)
            return render(request, "home.html")
        else:
            return HttpResponse("Email ou senha inválidos")


def home(request):
    return render(request, "home.html")


def criar_servico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return render("listar_servicos")
    else:
        form = ServicoForm()
    return render(request, "criar_servico.html", {"form": form})


@login_required(login_url="/auth/login/")
def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, "listar_servicos.html", {"servicos": servicos})


@login_required(login_url="/auth/login/")
def perfil(request):
    usuario = request.user
    return render(request, "perfil.html", {"usuario": usuario})
