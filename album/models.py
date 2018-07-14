from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')

class Photo(models.Model):
    description = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=50, default='')
    album_id = models.IntegerField(default=0)
    image = models.ImageField(upload_to='upload/images/', default='')