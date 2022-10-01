from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):

    context = {

    }
    return render(request, 'index.html', context)

def movie_list(request):
    
    context = {
        'img': 'https://nujhrcqkiwag1408085.cdn.ntruss.com/static/upload/movie_poster_images/movie_87793_1651545272.jpeg'
    }
    return render(request, 'movie_list.html', context)

def movie(request):

    context = {
        'img': 'https://nujhrcqkiwag1408085.cdn.ntruss.com/static/upload/movie_poster_images/movie_87793_1651545272.jpeg'
    }
    return render(request, 'movie.html', context)