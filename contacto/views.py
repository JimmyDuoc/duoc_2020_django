from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from .models import Contacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name','')
            email = request.POST.get('email','')
            phone = request.POST.get('phone','')
            
            caca = Contacto.objects.create(first_name=first_name,last_name=last_name,email=email,phone=phone)

            email = EmailMessage(
                "DUOC GYM - Contacto {} {}".format(first_name,last_name),
                "Nombre: {} {}\nCorreo Electrónico: {}\nTeléfono: {}".format(first_name,last_name,email,phone),
                "no-contestar@inbox.mailtrap.io",
                ["contacto@duocgym.cl"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contacto') + "?OK")
            except:
                return redirect(reverse('contacto') + "?FAIL") 

    return render(request,"contacto/contacto.html",{'form':contact_form})