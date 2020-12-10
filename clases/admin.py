from django.contrib import admin
from .models import Clase

# Register your models here.

class ClaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Clase,ClaseAdmin)
