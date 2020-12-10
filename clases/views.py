from django.shortcuts import render
from .models import Clase

# Create your views here.

def clases(request):
    clases = Clase.objects.all()
    return render(request,"clases/clases.html",{'clases':clases})