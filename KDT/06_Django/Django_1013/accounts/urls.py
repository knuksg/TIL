from . import views
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('<int:user_pk>/followers/', views.followers, name='followers'),
    path('<int:user_pk>/followings/', views.followings, name='followings'),
]