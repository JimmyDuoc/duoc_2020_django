from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Nombre")
    image = models.ImageField(verbose_name = "Imagen",upload_to="instructor")
    specialty = models.CharField(max_length = 100, verbose_name = "Especialidad")
    experience = models.TextField(verbose_name = "Experiencia")
    facebook = models.CharField(max_length = 100, verbose_name = "Facebook")
    twitter = models.CharField(max_length = 100, verbose_name = "Twitter")
    instagram = models.CharField(max_length = 100, verbose_name = "Instagram")
    created = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha Creación")
    updated = models.DateTimeField(auto_now = True, verbose_name= "Fecha Modificación")
    
class Meta:
    verbose_name = "instructor"
    verbose_name_plural = "instructores"
    ordering = ['-updated','-created']

def __str__(self):
    return self.name