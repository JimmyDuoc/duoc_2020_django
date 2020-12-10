from django.contrib import admin
from .models import Instructor

# Register your models here.

class InstructorAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Instructor,InstructorAdmin)