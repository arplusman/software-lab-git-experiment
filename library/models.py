from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_data = models.DateField()
    created = models.DateTimeField(auto_now=True)
    email = models.EmailField()


class Book(models.Model):
    name = models.CharField()
    year = models.IntegerField()
    number_of_pages = models.IntegerField()
    edition = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
