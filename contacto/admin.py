from django.contrib import admin

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Contacto,ContactoAdmin)