from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class CreateAuthor(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    