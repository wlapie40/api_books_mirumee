from django.core.management.base import BaseCommand, CommandError
import csv
from .upload_model import ModelUploader


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)
        parser.add_argument('model', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'][0]) as csvfile:
            next(csvfile)
            reader = csv.reader(csvfile, delimiter=';', quotechar="'")
            model = options['model'][0]
            ModelUploader().upload_books(reader) if model == "Books" else ModelUploader.upload_rates(reader)
