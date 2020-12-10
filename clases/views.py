from django.shortcuts import render

# Create your views here.

def clases(request):
    return render(request,"clases/clases.html")