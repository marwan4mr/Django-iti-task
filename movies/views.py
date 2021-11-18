from django.shortcuts import redirect, render
from django.http import HttpResponse
from .form import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required

# we will get this from the database 
movie_list = []
# Create your views here.
@login_required
def index(request):
    # return HttpResponse('hello fuckface')
    return render(request, 'movies/index.html', context={ 'movie_list': Movie.objects.all()} )
# 
def add_movie(request):
    if request.method == 'GET':
        return render(request, 'movies/movie_add.html', context={ 'form': MovieForm() })
    elif request.method == "POST":
        form = MovieForm(data=request.POST, files=request.FILES, instance=Movie)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # print(form.cleaned_data)
            print(form.cleaned_data)
            # m = Movie(**form.cleaned_data)
            # m.save()
            form.save()
            return redirect('movies:index')
        else:
            return render(request, 'movies/movie_add.html', context={ 'form': form })

def home(request):
    return render(request, 'base.html')