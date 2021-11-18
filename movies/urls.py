from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    # there will probably be namespace collision with the index name we'll see about that later
    # name spacing solves this issue as you can see app_name over ther and {% url 'movies:index' %}
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('add', views.add_movie, name="add")
]