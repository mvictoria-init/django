# Generated by Django 5.1.2 on 2024-12-20 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-created'], 'verbose_name': 'PeliculaGhibli', 'verbose_name_plural': 'PeliculasGhibli'},
        ),
    ]
