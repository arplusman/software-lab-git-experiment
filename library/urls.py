from django.urls import path
from .views import *

urlpatterns = [
    path('author/crate', CreateAuthor.as_view()),
]