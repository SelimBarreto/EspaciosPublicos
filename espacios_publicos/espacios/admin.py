from django.contrib import admin
from .models import InstalacionDeportiva, Cancha

@admin.register(InstalacionDeportiva)
class InstalacionDeportivaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'alcaldia', 'deporte', 'acepta_mascotas')

@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    list_display = ('id', 'etiqueta', 'deporte', 'espacio')
