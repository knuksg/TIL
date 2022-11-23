from django.shortcuts import get_object_or_404, redirect, render
from articles.models import Article
from movies.models import Movie
from movies.forms import MovieForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
        else:
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form':form
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    articles = Article.objects.filter(movie=movie)
    sum = 0
    count = 0
    for article in articles:
        sum += article.grade
        count += 1
    if sum:
        avg_grade = round(sum/count, 2)
    else:
        avg_grade = 0
    context = {
        'movie': movie,
        'avg_grade': avg_grade,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form
    }
    return render(request, 'movies/update.html', context)

@login_required
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')