from django.shortcuts import get_object_or_404, redirect, render
from articles.models import Article
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users':users
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)    
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    articles = user.article_set.all()[0:2]
    like_articles = user.like_articles.all()[0:2]
    # 평균 별점
    sum_users = Article.objects.filter(user=user)
    sum = 0
    count = 0
    for sum_user in sum_users:
        sum += sum_user.grade
        count += 1
    if sum:
        avg_user = round(sum/count, 2)
    else:
        avg_user = 0
    context = {
        'user': user,
        'articles': articles,
        'like_articles': like_articles,
        'avg_user': avg_user,
    }
    return render(request, 'accounts/detail.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

@login_required
def follow(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if request.user in user.followings.all():
        user.followings.remove(request.user)
    else:
        user.followings.add(request.user)
    return redirect('accounts:detail', user_pk)

def followers(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    followers = user.followers.all()
    context = {
        'user': user,
        'followers': followers,
    }
    return render(request, 'accounts/followers.html', context)

def followings(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    followings = user.followings.all()
    context = {
        'user': user,
        'followings': followings,
    }
    return render(request, 'accounts/followings.html', context)