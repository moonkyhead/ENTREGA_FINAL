from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def saludar(request):
    return HttpResponse('Lo de Leandrito')

def saludar_con_etiqueta(request):
    return HttpResponse('<h1> La mejor Musica Trascendental</h1>')

def saludar_con_parametros(request, nombre: str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f'{apellido}, {nombre}')

def index(request):
    return render(request,'core/index.html') 