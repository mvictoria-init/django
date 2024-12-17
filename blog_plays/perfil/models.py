from django.db import models

# Create your models here.

class Proyect(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    desc = models.TextField(verbose_name='Descripcíon')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'
        
        def __str__(self):
            return self.title