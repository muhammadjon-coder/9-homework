from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_year = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=200)
