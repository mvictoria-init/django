from django.urls import path

from . import views

urlpatterns = [
    path('history', views.history, name='history'),
    path('', views.home, name='homes'),
    path('other/<page_id>', views.other, name='other'),
    path('visit', views.visit, name='visit'),
]
