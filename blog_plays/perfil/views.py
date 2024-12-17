from django.shortcuts import render

# models
from .models import Proyect

# Create your views here.
def profile(request):
    proyects = Proyect.objects.all()
    return render(request, 'profile.html', {'proyects':proyects})