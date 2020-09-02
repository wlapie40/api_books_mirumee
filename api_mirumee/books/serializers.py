from rest_framework import serializers
from .models import (Authors,
                     Books,
                     Rates)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ("id", "author", "created_at")


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = "__all__"


class BooksSerializer(serializers.ModelSerializer):
    comments = RatesSerializer(many=True, read_only=True)

    class Meta:
        model = Books
        fields = ("id", "isbn", "title", "author", "genres", "created_at", "comments",)
