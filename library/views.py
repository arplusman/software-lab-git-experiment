from django.shortcuts import render
from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer

class CreateAuthor(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
