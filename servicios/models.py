from django.db import models

# Create your models here.

class Servicio(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Título")
    icon = models.CharField(max_length = 100, verbose_name = "Icono")
    description = models.TextField(verbose_name = "Descripción")
    created = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha Creación")
    updated = models.DateTimeField(auto_now = True, verbose_name= "Fecha Modificación")
    
class Meta:
    verbose_name = "servicio"
    verbose_name_plural = "servicios"
    ordering = ['-updated','-created']

def __str__(self):
    return self.title