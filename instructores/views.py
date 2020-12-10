from django.shortcuts import render
from .models import Instructor

# Create your views here.

def instructores(request):
    instructores = Instructor.objects.all()
    return render(request,"instructores/instructores.html",{'instructores':instructores})