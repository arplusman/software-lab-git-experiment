from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_data = models.DateField()
    created = models.DateTimeField(auto_now=True)
    email = models.EmailField()
