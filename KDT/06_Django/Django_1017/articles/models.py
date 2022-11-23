from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                    processors=[ResizeToFill(300, 300)],
                                    format='JPEG',
                                    options={'quality': 80})
                                
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()