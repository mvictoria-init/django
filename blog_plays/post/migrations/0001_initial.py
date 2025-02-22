# Generated by Django 5.1.2 on 2024-12-17 19:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog', verbose_name='Imagen')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('desc', models.TextField(verbose_name='Descripción')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
                'ordering': ['created'],
            },
        ),
    ]
