from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class ListApps(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    
    description = models.TextField(verbose_name='Descripción')
    
    image = models.ImageField(verbose_name='Imagen', upload_to='list_apps')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    tecno= models.TextField(verbose_name='Técnologías')
    
    url = models.CharField(max_length=100, verbose_name='Dirección web')
    
    githud = models.BooleanField(verbose_name='Githud')
        
    githud_url = models.CharField(max_length=100, verbose_name='Public')

    class Meta: 
        verbose_name = 'ListApp'
        verbose_name_plural = 'ListApps'
        ordering = ['-created']