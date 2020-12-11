from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label="Nombre", min_length=3, max_length=100, required=True)
    last_name = forms.CharField(label="Apellido", min_length=3, max_length=100, required=True)
    email = forms.EmailField(label="Correo Electrónico", min_length=5, max_length=100, required=True)
    phone = forms.CharField(label="Teléfono", min_length=9, max_length=12, required=True)