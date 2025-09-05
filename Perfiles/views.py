from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def inicio(request):
    return render(request, 'pagInicio.html',{})

def formulario(request):
    return render(request, 'formulario.html',{})