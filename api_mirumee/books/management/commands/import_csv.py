import csv
from contextlib import contextmanager

from django.core.management.base import BaseCommand

from .upload_model import ModelUploader


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)
        parser.add_argument('model', nargs='+', type=str)

    @staticmethod
    def check_file_format(filename: str = None):
        """
        For security reasons, we want to be sure that .csv
        file is being provided not .sh or any other harm file.
        :param filename: the name of the file to check
        :return: True if the provided file has the .csv extension
        in any other case False is being returned
        """
        accepted_file_types = ["csv"]

        if filename.split(".")[-1] in accepted_file_types:
            return True
        return False

    @staticmethod
    def csv_sniffer(file: object = None, read_lines: int = 1024):
        """
        :param file: an opened file object
        :param read_lines: the number of first lines to check
        :return: True if correct csv file was provided
        """
        try:
            csv.Sniffer().sniff(file.read(read_lines))
            file.seek(0)
            return True
        except csv.Error:
            raise ValueError("Wrong file format")

    @staticmethod
    @contextmanager
    def managed_file(file):
        try:
            f = open(file)
            yield f
        finally:
            f.close()

    def handle(self, *args, **options):
        filename = options['csv_file'][0]

        if self.check_file_format(filename):
            with self.managed_file(filename) as csvfile:

                self.csv_sniffer(csvfile)

                next(csvfile)
                reader = csv.reader(csvfile, delimiter=';', quotechar="'")
                model = options['model'][0]
                ModelUploader().add_book_model(reader) if model == "Books" else ModelUploader.add_rates_model(reader)
        else:
            raise ValueError("Wrong file format")
