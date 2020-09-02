from books.models import (Authors,
                          Books,
                          Rates)
from django.test import TestCase


class AuthorTest(TestCase):
    def setUp(self):
        Authors.objects.create(author="Sandipan Dey", id="f40f097a-36fc-47b8-bcea-5f3f25a919df")
        Authors.objects.create(author="Eric van Rees", id="74999557-0632-41ea-90e9-fa29c6f3e2bf")

    def test_author_creation(self):
        author_1 = Authors.objects.get(author="Sandipan Dey")
        author_2 = Authors.objects.get(author="Eric van Rees")
        self.assertTrue(author_1.id, "f40f097a-36fc-47b8-bcea-5f3f25a919df")
        self.assertTrue(author_2.id, "74999557-0632-41ea-90e9-fa29c6f3e2bf")


class BooksTest(TestCase):
    def setUp(self):
        author_1 = Authors.objects.create(author="Sandipan Dey", id="f40f097a-36fc-47b8-bcea-5f3f25a919df")
        Books.objects.create(title="Hands-On Image Processing with Python", isbn="9781789341850", author=author_1)
        Books.objects.create(title="Python Image Processing Cookbook", isbn="9781789537147", author=author_1)

    def test_books_creation(self):
        book_1 = Books.objects.get(isbn="9781789341850")
        book_2 = Books.objects.get(isbn="9781789341850")
        self.assertTrue(book_1.title, "Hands-On Image Processing with Python")
        self.assertTrue(book_2.title, "Python Image Processing Cookbook")


class RatesTest(TestCase):
    def setUp(self):
        author_1 = Authors.objects.create(author="Sandipan Dey", id="f40f097a-36fc-47b8-bcea-5f3f25a919df")
        book_1 = Books.objects.create(
            title="Hands-On Image Processing with Python", isbn="9781789341850", author=author_1)
        Rates.objects.create(book=book_1, rate=4, text="not bad")
        Rates.objects.create(book=book_1, rate=3, text="test2")

    def test_books_creation(self):
        rates = Rates.objects.all()
        self.assertTrue(len(rates), 2)
