from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer, UserSerializer
from .models import Author, Book
from django.contrib.auth.models import User


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
