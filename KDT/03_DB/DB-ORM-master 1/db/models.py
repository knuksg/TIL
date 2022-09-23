from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()

Director.objects.create(name='봉준호', debut='1993-01-01', country='KOR')
Director.objects.create(name='김한민', debut='1999-01-01', country='KOR')
Director.objects.create(name='최동훈', debut='2004-01-01', country='KOR')
Director.objects.create(name='이정재', debut='2022-01-01', country='KOR')
Director.objects.create(name='이경규', debut='1992-01-01', country='KOR')
Director.objects.create(name='한재림', debut='2005-01-01', country='KOR')
Director.objects.create(name='Joseph Kosinski', debut='1999-01-01', country='KOR')
Director.objects.create(name='김철수', debut='2022-01-01', country='KOR')

Genre.objects.create(title='액션')
Genre.objects.create(title='드라마')
Genre.objects.create(title='사극')
Genre.objects.create(title='범죄')
Genre.objects.create(title='스릴러')
Genre.objects.create(title='SF')
Genre.objects.create(title='무협')
Genre.objects.create(title='첩보')
Genre.objects.create(title='재난')