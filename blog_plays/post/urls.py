
from django.urls import path

# views
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:id>/', views.post, name='post'),
]
