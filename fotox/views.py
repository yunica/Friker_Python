from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Foto
from .forms import FormularioFoto


def home(request):
    # return HttpResponse("Hello, world. You're at the polls index :3.")
    return render(request, 'fotox/principal.html', {})


def agregar(request):
    context = {
        "saludo": 18,
        "despedida": 50,
    }
    return render(request, 'fotox/index.html', context)


def mostrar(request):
    lista = Foto.objects.all()
    return render(request, 'fotox/pagina2.html', {'list': lista})


@login_required()
def mostrarformulario(request):
    if request.method == "POST":
        formulario = FormularioFoto(request.POST)
        if formulario.is_valid():
            foto = formulario.save(commit=False)
            foto.fecha_creacion = timezone.now()
            foto.save()
            return redirect('mostrar')
    else:
        formulario = FormularioFoto()

    return render(request, 'fotox/formm.html', {'formx': formulario})


def mostrar2(request, pedido):
    try:
        lista = Foto.objects.get(apellido=pedido)
    except Foto.DoesNotExist:
        raise Http404('Este Id no fue encontrado :( ', pedido)

    return render(request, 'fotox/pagina2.html', {'list': lista})


def ingresar(request):
    username = request.POST['username']
    password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #   login(request, user)
    return render(request, 'fotox/login.html', {})


def buscarajax(request):
    nom = request.GET['foto']

    return render(request, 'fotox/formm.html', {'nom': nom})
