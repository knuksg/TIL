from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

from articles.models import Article


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(70, 100)],
                                format='JPEG',
                                options={'quality': 60})

    def __str__(self):
        return self.title

    @property
    def avg_grade(self):
        movies = Article.objects.filter(movie=self)
        if movies:
            total_grade = 0
            count = 0
            for movie in movies:
                total_grade += movie.grade
                count += 1
            return total_grade / count
        else:
            return 0
