from django.core.management import call_command
from django.test import TestCase
from books.models import (Authors,
                          Books,
                          Rates)


class CommandsTestCase(TestCase):

    @staticmethod
    def add_books():
        args = ["ksiazki.csv", "Books"]
        opts = {}
        call_command('import_csv', *args, **opts)

    def test_invalid_file_extension(self):
        with self.assertRaisesMessage(ValueError, "Wrong file format"):
            args = ["ksiazki.sh", "Books"]
            opts = {}
            call_command('import_csv', *args, **opts)

    def test_add_books(self):
        args = ["ksiazki.csv", "Books"]
        opts = {}
        call_command('import_csv', *args, **opts)
        self.assertEqual(Books.objects.count(), 5)
        self.assertEqual(Authors.objects.count(), 5)

    def test_add_rates_without_books(self):
        args = ["opinie.csv", "Rates"]
        opts = {}
        call_command('import_csv', *args, **opts)
        self.assertEqual(Rates.objects.count(), 0)

    def test_add_books_and_rates(self):
        self.add_books()

        args = ["opinie.csv", "Rates"]
        opts = {}
        call_command('import_csv', *args, **opts)
        self.assertEqual(Rates.objects.count(), 11)
