from rest_framework import viewsets

from .models import (Authors,
                     Books,
                     Rates)
from .serializers import (AuthorSerializer,
                          BooksSerializer,
                          RatesSerializer)


class AuthorViewV1(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class BooksViewV1(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class RatesViewV1(viewsets.ModelViewSet):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer

