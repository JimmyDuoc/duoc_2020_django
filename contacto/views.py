from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def contacto(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            #first_name = request.POST.get('name','')
            #last_name = request.POST.get('last_name','')
            #email = request.POST.get('email','')
            #phone = request.POST.get('phone','')
            #ContactForm = form.save()
            return redirect(reverse('contacto') + "?OK")

    return render(request,"contacto/contacto.html",{'form':contact_form})