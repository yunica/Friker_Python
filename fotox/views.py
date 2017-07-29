from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def agregar(request):
    return HttpResponse("Esta es una vista para agregar.")
