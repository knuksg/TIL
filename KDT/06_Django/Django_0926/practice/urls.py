from django.urls import path
from . import views

urlpatterns = [
    path("is-odd-even/<int:number>", views.is_odd_even),
    path("calculate/<int:number1>/<int:number2>", views.calculate),
    path("random-game/", views.random_game),
    path("result/", views.result),
    path("lipsum/", views.lipsum),
    path("lipsum-result/", views.lipsum_result),
    path("index/", views.index),
]
