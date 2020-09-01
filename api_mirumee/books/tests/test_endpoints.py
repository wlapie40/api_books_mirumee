from books.models import (Authors,
                          Books,
                          Rates)
from rest_framework import status
from rest_framework.test import APITestCase


class AuthorTestV1(APITestCase):
    def setUp(self):
        author_1 = Authors.objects.create(author="Sandipan Dey", id="f40f097a-36fc-47b8-bcea-5f3f25a919df")
        Books.objects.create(title="Python Image Processing Cookbook",
                             isbn="9781789537147",
                             author=author_1,
                             genres="Education")

    def test_create_author(self):
        data = {'author': 'Adam Mickiewicz'}
        response = self.client.post("http://localhost:8000/api/v1/authors/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Authors.objects.count(), 2)
        self.assertEqual(Authors.objects.get(author='Adam Mickiewicz').author, 'Adam Mickiewicz')

    def test_list_authors(self):
        response = self.client.get("http://localhost:8000/api/v1/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Authors.objects.count(), 1)


class BooksTestV1(APITestCase):
    def setUp(self):
        author_1 = Authors.objects.create(author="Sandipan Dey", id="f40f097a-36fc-47b8-bcea-5f3f25a919df")
        Books.objects.create(title="Python Image Processing Cookbook",
                             isbn="9781789537147",
                             author=author_1,
                             genres="Education")
        Books.objects.create(title="Python OpenCV",
                             isbn="9781789537146",
                             author=author_1,
                             genres="Education")

    def test_create_book(self):
        data = {"isbn": "9788366436571",
                "title": "Test",
                "author": "f40f097a-36fc-47b8-bcea-5f3f25a919df",
                "genres": "Kryminał"}
        response = self.client.post("http://localhost:8000/api/v1/books/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Books.objects.count(), 3)
        self.assertEqual(Books.objects.get(title="Test").title, 'Test')

    def test_list_books(self):
        response = self.client.get("http://localhost:8000/api/v1/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Books.objects.count(), 2)

    def test_list_book_by_title(self):
        response = self.client.get("http://localhost:8000/api/v1/books/Python Image Processing Cookbook/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RatesTestV1(APITestCase):
    def setUp(self):
        author_1 = Authors.objects.create(author="Sandipan Dey", id="f40f097a-36fc-47b8-bcea-5f3f25a919df")
        book_1 = Books.objects.create(id="3fec8f9d-b439-4d64-b219-21b77d017850",
                             title="Python Image Processing Cookbook",
                             isbn="9781789537147",
                             author=author_1,
                             genres="Education")
        Rates.objects.create(book_id=book_1,
                             rate=4,
                             text="Education")

    def test_create_rate(self):
        data = {"book_id": "3fec8f9d-b439-4d64-b219-21b77d017850",
                "rate": "3",
                "text": "test rate"}
        response = self.client.post("http://localhost:8000/api/v1/rates/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rates.objects.count(), 2)
        self.assertEqual(Rates.objects.get(text="test rate").text, "test rate")

    def test_list_rates(self):
        response = self.client.get("http://localhost:8000/api/v1/rates/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Rates.objects.count(), 1)
