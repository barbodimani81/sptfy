from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
