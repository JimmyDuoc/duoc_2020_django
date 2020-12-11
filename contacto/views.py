from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def contacto(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            return redirect(reverse('contacto') + "?OK")
        else:
            return redirect(reverse('contacto') + "?FAIL")

    return render(request,"contacto/contacto.html",{'form':contact_form})