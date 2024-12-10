from django.shortcuts import render, redirect
from .models import Movie


def home(request):
    return render(request, 'index.html')


def movie_list(request):
    movies = Movie.objects.all()
    ctx = {'movies': movies}
    return render(request, "movies/list.html", ctx)


from django.shortcuts import render, redirect
from .models import Movie


def movie_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')

        if title and director and release_year and genre:
            Movie.objects.create(
                title=title,
                director=director,
                release_year=release_year,
                genre=genre
            )
            return redirect('movies:list')

        return render(request, 'movies/form.html', {
            'error': 'Barcha maydonlarni to‘ldiring!'
        })

    return render(request, 'movies/form.html')
