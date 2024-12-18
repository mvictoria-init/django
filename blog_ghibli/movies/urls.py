from django.urls import path

from .views import movieGhibli, movie_view

urlpatterns = [
    path('', movieGhibli, name='movies'),
    path('<str:movie_url>/', movie_view, name='movie_detail'),
]
