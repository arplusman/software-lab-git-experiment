from django.urls import path
from .views import *

urlpatterns = [
    path('author/crate/', CreateAuthor.as_view()),
    path('author/list/', ListAuthor.as_view()),
    path('book/create/', CreateBook.as_view()),
    path('book/list/', ListBook.as_view()),
]