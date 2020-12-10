from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"core/inicio.html")

def servicios(request):
    return render(request,"core/servicios.html")

def instructores(request):
    return render(request,"core/instructores.html")

def contacto(request):
    return render(request,"core/contacto.html")