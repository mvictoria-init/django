from django.urls import path

from .views import about_fan

urlpatterns = [
    path('acerca_de_fan', about_fan, name='about_fan'),
]
