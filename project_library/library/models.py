from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}({self.author.name})'
