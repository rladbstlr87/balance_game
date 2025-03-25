from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)

    