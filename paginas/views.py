from django.shortcuts import render
from django.http import HttpResponse


#Crear vistas aquí
def vista_pagina_inicio(request):
    return HttpResponse("<h1>Página de inicio</h1>")

def about(request):
    context = {'nombre':'Alejandro',
               'edad' : 20}
    return render(request, 'paginas/about.html',context)
