from books.models import (Authors,
                          Books,
                          Rates)

from .logger import logger


class ModelUploader:

    @classmethod
    def add_books_model(cls, data: list):
        """
        Add records to the database specified in the settings.py.
        With the very first step function checks if a provided author exists in the database,
        in case there is no result, the new author is being created based on received data
        :param data:
        """
        try:
            for row in data:
                author = Authors.objects.filter(author=row[2]).first()
                if not author:
                    logger.info(f"There is no record: {row[2]}")
                    Authors.objects.create(author=row[2])
                    logger.info(f"{row[2]} added")

                book = Books.objects.filter(isbn=row[0]).first()
                if book:
                    logger.info(f'ISBN {row[0]} exists')
                    continue
                author = Authors.objects.get(author=row[2])
                Books.objects.create(title=row[1], isbn=row[0], author=author, genres=row[3])
                logger.info(f'Added book with ISBN: {row[0]}')
        except Exception as e:
            logger.error(f"msg: {e}")

    @classmethod
    def add_rates_model(cls, data: list):
        """
          Add records to the database specified in the settings.py.
          With the very first step function checks, if a provided ISBN number exists in the database,
          in case there is no result, the function skips the record and moves to the next one.
          :param data:
          """
        try:
            for row in data:
                book = Books.objects.filter(isbn=row[0]).first()
                if book:
                    book_instance = Books.objects.get(isbn=row[0])
                    Rates.objects.create(book=book_instance,
                                         rate=row[1],
                                         text=row[2])
                    logger.info(f'Rates added')
                else:
                    logger.info(f'ISBN {row[0]} does not exists')
        except Exception as e:
            logger.error(f"msg: {e}")
