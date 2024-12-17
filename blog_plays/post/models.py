from django.db import models

# ckeditor 
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='blog')
    title = models.CharField(max_length=200, verbose_name='Título')
    desc = models.TextField(verbose_name='Descripción')
    content = RichTextField(verbose_name='Contenido')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        # cambiar el nombre en el menu principal
        verbose_name='Publicación'
        # cambiar el nombre en el menu principal
        verbose_name_plural='Publicaciones'
        # ordenar elementos del ultimo al primero
        ordering = ['created']
        
    def __str__(self):
        return self.title
