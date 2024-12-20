from django.urls import path

from .views import ListAppView

urlpatterns = [
    path('', ListAppView),
]
