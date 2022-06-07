from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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


class Review(models.Model):

    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    watchlist = models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.watchlist.title + '  ||  ' + str(self.rating)