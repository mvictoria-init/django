from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Movie

# Create your views here.

def movieGhibli(request):
    movies = Movie.objects.all().order_by('-created')
    
    paginator = Paginator(movies, 3)
    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # Si la página no es un entero, muestra la primera página
        page = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, muestra la última página
        page = paginator.page(paginator.num_pages)
    
    return render(request, 'index_ghibli.html', {'page': page})

def movie_view(request, movie_url):
    movie = get_object_or_404(Movie, url=movie_url)
    return render(request, 'movie_ghibli.html', {'movie': movie})

