from django.db import models
from articles.models import Article
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    @property
    def avg_grade(self):
        movies = Article.objects.filter(user=self)
        total_grade = 0
        count = 0
        for movie in movies:
            total_grade += movie.grade
            count += 1
        if count > 5:
            return round(total_grade / count, 1)
        else:
            return "평가한 영화 5개 이하"