from django.db import models

# Create your models here.

class Movie(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Watchlist(models.Model):

    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist',null=True,blank=True)

    def __str__(self):
        return self.title