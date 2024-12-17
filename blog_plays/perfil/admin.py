from django.contrib import admin

from .models import Proyect

# Register your models here.

# registar un modelo en el django admin... de forma simple
# admin.site.register(Proyect)

# registar un modelo en el django admin... de forma avanzada
@admin.register(Proyect)
class ProyectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created',)
    # poner links en el elemento
    list_display_links = ('title',)
    # lista editable
    list_editable = ('desc',)
    # filtrar
    list_filter = ('title', 'created', 'update',)
    # buscar
    search_fields = ('title',)
    # solo lectura
    readonly_fields = ('created', 'update',)