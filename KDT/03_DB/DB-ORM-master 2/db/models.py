from turtle import title
from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()

class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()
    screening = models.BooleanField()

person =  Director.objects.get(name='봉준호')
print(f'id : {person.id}')
print(f'name : {person.name}')
print(f'debut : {person.debut}')
print(f'country : {person.country}')

g1 = Genre.objects.get(title='드라마')
print(f'id : {g1.id}')
print(f'title : {g1.title}')



director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

movie = Movie()

movie.director = director_
movie.genre = genre_
movie.title = '기생충'
movie.opening_date = '2019-05-30'
movie.running_time = 132
movie.screening = False

movie.save()

movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for movie in movies:
    director_ = Director.objects.get(name=movie[0])
    genre_ = Genre.objects.get(title=movie[1])
    title_ = movie[2]
    opening_date_ = movie[3]
    running_time_ = movie[4]
    screening_ = movie[5]
    Movie.objects.create(director=director_, genre=genre_, title=title_, opening_date=opening_date_, running_time=running_time_, screening=screening_)

for data in Movie.objects.all():
    print(data.director, data.genre, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all():
    print(data.director.name, data.genre, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all():
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all().order_by('-opening_date'):
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all().order_by('opening_date'):
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)
    break

for data in Movie.objects.all().order_by('opening_date').filter(screening=True):
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all().order_by('opening_date').filter(director_id=Director.objects.get(name='봉준호')):
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)

data = Movie.objects.all().order_by('opening_date').filter(director_id=Director.objects.get(name='봉준호'))[1]
print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all().order_by('opening_date').filter(running_time__gt=119).order_by('running_time'):
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all().order_by('opening_date').filter(running_time__gte=119).order_by('running_time'):
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all().order_by('opening_date').filter(opening_date__gte='2022-01-01').order_by('opening_date'):
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)

for data in Movie.objects.all().exclude(director=Director.objects.get(name='봉준호')).order_by('opening_date'):
    print(data.director.name, data.genre.title, data.title, data.opening_date, data.running_time, data.screening)