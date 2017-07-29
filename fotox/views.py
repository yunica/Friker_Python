from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Foto


def home(request):
    return HttpResponse("Hello, world. You're at the polls index :3.")


def agregar(request):
    context = {
        "saludo": 18,
        "despedida": 50,
    }
    return render(request, 'fotox/index.html', context)


def mostrar(request):
    lista = Foto.objects.all()
    return render(request, 'fotox/pagina2.html', {'list': lista})


def mostrar2(request, pedido):
    try:
        lista = Foto.objects.get(apellido=pedido)
    except Foto.DoesNotExist:
        raise Http404('Este Id no fue encontrado :( ')

    return render(request, 'fotox/pagina2.html', {'list': lista})
