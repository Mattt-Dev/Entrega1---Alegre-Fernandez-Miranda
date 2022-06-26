from django.contrib import admin

from .models import *
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_inicio', 'profesor', 'comision')

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre_evento','fecha_inicio','disertante')

class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_nacimiento','estudios', 'acerca_de')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Nosotros, NosotrosAdmin)