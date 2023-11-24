from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "landing/index.html")
#Crear un def por pestaña

def nosotros(request):
    return render(request, "landing/nosotros.html")
#Crear un def por pestaña

def contacto(request):
    return render(request, "landing/contacto.html")