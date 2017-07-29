from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def agregar(request):
    context = {
        "saludo": 18,
        "despedida": 50,
    }
    return render(request, 'fotox/index.html', context)





