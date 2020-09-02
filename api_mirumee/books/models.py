import uuid

from django.core.validators import (MinValueValidator,
                                    MaxValueValidator)
from django.db import models


class Authors(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: {0}, author: {1}, created_at: {2}"\
            .format(self.id, self.author, self.created_at)

    class Meta:
        ordering = ['author']


class Books(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        Authors,
        on_delete=models.CASCADE)
    genres = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: {0}, isbn: {1}, title: {2}, author: {3}, genres: {4}, created_at: {5}"\
            .format(self.id, self.isbn, self.title, self.author, self.genres, self.created_at)

    class Meta:
        ordering = ['isbn']


class Rates(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    book_id = models.ForeignKey(
        Books,
        on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    text = models.TextField(max_length=300)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: {0}, book_id: {1}, rate: {2}, text: {3}, pub_date: {4}"\
            .format(self.id, self.book_id, self.rate, self.text, self.pub_date)

    class Meta:
        ordering = ['pub_date']
