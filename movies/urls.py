from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('list/', views.movie_list, name='list'),
    path('create/', views.movie_create, name='create'),
]
