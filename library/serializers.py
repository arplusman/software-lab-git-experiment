from rest_framework.serializers import ModelSerializer
from .models import Author, Book

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date', 'email']


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'year', 'number_of_pages', 'edition', 'author']
