from django.contrib import admin

from .models import ListApps

# Register your models here.

@admin.register(ListApps)
class ListAppsAdmin(admin.ModelAdmin):
    # escoger que elementos se veran en la vista como una lista
    list_display = ('id', 'title', 'description', 'created',)
    # poner links en el elemento
    list_display_links = ('title',)
    # solo lectura
    readonly_fields = ('created',)