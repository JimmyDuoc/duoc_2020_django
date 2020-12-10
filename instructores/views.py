from django.shortcuts import render

# Create your views here.

def instructores(request):
    return render(request,"instructores/instructores.html")