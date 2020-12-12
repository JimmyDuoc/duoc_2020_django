from django.db import models

# Create your models here.

class Contacto(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Nombre")
    last_name = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.CharField(max_length=100, verbose_name="Correo Electrónico")
    phone = models.CharField(max_length=12, verbose_name="Teléfono")
    created = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha Creación")
    
    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
        ordering = ['-created']

    def __str__(self):
        return self.email

