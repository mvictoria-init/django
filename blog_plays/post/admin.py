from django.contrib import admin

from .models import Post

# Register your models here.

# registar un modelo en el django admin... de forma simple
# admin.site.register(Post)

# que salgan todos los elementos en una tabla
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # escoger que elementos se veran en la vista como una lista
    list_display = ('id', 'image', 'title', 'desc', 'created')
    # poner links en el elemento
    list_display_links = ('id', 'title')
    # filtrar
    list_filter = ('created', 'update')
    # buscar
    search_fields = ('title', 'desc')
    # solo lectura
    readonly_fields = ('created', 'update')