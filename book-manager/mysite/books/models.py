from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User
from django.utils import timezone


class Book(models.Model):
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title + ' - ' + self.author


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)


class Review(models.Model):
    book = models.ForeignKey('Book', related_name='reviews')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
