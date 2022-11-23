"""django_0922 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# app[training]/views.py 불러오기
from training import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('template/', views.template),
    path('todaydinner/', views.todaydinner),
    path('lottery/', views.lottery),
    path('form/', views.form),
    path('ping/', views.ping),
    path('pong/', views.pong),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)