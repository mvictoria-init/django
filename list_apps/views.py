from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ListApps

# Create your views here.

def ListAppView(request):
    list = ListApps.objects.all().order_by('-created')
    
    paginator = Paginator(list, 6)
    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # Si la página no es un entero, muestra la primera página
        page = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, muestra la última página
        page = paginator.page(paginator.num_pages)
    
    return render(request, 'index_listapps.html', {'page': page})