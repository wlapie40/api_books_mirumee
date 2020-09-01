from django.shortcuts import render
from rest_framework import viewsets
from .models import (Authors,
                     Books,
                     Rates)
from .serializers import (AuthorSerializer,
                          BooksSerializer,
                          RatesSerializer)


class AuthorView(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class RatesView(viewsets.ModelViewSet):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer

