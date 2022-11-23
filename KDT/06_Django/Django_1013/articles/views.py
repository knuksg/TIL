from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from articles.models import Article, Comment
from movies.models import Movie
from articles.forms import ArticleForm, MovieArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    paginator = Paginator(articles, 5)
    page_obj = paginator.get_page(page)
    context = {
        'articles':page_obj
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
        else:
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

@login_required
def article_create(request, movie_pk):
    if request.method == 'POST':
        form = MovieArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.movie = Movie.objects.get(pk=movie_pk)
            article.save()
            return redirect('articles:index')
        else:
            return redirect('articles:index')
    else:
        form = MovieArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    movie = article.movie
    comments = article.comment_set.all()
    comment_form = CommentForm()
    sum_articles = Article.objects.filter(movie=movie)
    sum = 0
    count = 0
    for sum_article in sum_articles:
        sum += sum_article.grade
        count += 1
    if sum:
        avg_grade = round(sum/count, 2)
    else:
        avg_grade = 0
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'avg_grade': avg_grade,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@login_required
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        context = {
            'content': comment.content,
            'created_at': comment.created_at,
            'userName': comment.user.username,
            'avg_grade': comment.user.avg_grade,
        }
        return JsonResponse(context)
    return redirect('articles:detail', pk)

@login_required
def comment_delete(request, article_pk, comment_pk):
    print(request.POST)
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

@login_required
def like(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user in article.like_users.all(): 
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', pk)
