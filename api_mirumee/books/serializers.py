from rest_framework import serializers
from .models import (Authors,
                     Books,
                     Rates)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ("id",
                  "author",
                  "created_at")


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ("id", "isbn", "title", "author", "genres", "created_at")


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = ("id", "book_id", "rate", "text", "pub_date")
