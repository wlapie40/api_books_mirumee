import csv
from contextlib import contextmanager

from django.core.management.base import BaseCommand

from .upload_model import ModelUploader


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)
        parser.add_argument('model', nargs='+', type=str)

    @staticmethod
    @contextmanager
    def managed_file(file):
        try:
            f = open(file)
            yield f
        finally:
            f.close()

    def handle(self, *args, **options):
        with self.managed_file(options['csv_file'][0]) as csvfile:
            next(csvfile)
            reader = csv.reader(csvfile, delimiter=';', quotechar="'")
            model = options['model'][0]
            ModelUploader().add_book_model(reader) if model == "Books" else ModelUploader.add_rates_model(reader)