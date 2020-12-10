from django.db import models

# Create your models here.

class Clase(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Título")
    image = models.ImageField(verbose_name = "Imagen",upload_to="clase")
    instructor = models.CharField(max_length = 100, verbose_name = "Instructor")
    created = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha Creación")
    updated = models.DateTimeField(auto_now = True, verbose_name= "Fecha Modificación")
    
class Meta:
    verbose_name = "clase"
    verbose_name_plural = "clases"
    ordering = ['-updated','-created']

def __str__(self):
    return self.title
