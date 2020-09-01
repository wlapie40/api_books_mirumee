from books.models import (Authors,
                          Books,
                          Rates)

from .logger import logger


class ModelUploader:

    @classmethod
    def upload_books(cls, data):
        for row in data:
            author = Authors.objects.filter(author=row[2]).first()
            if not author:
                logger.info(f"We don't have author {row[2]}")
                Authors.objects.create(author=row[2])
                logger.info(f"{row[2]} Added")

            book = Books.objects.filter(isbn=row[0]).first()
            if book:
                logger.info(f'isbn {row[0]} exists')
                continue
            logger.info(f'Adding book isbn {row[0]}')
            author = Authors.objects.get(author=row[2])
            Books.objects.create(title=row[1], isbn=row[0], author=author, genres=row[3])

    @classmethod
    def upload_rates(cls, data):
        for row in data:
            book = Books.objects.filter(isbn=row[0]).first()
            if book:
                book_instance = Books.objects.get(isbn=row[0])
                Rates.objects.create(book_id=book_instance,
                                     rate=row[1],
                                     text=row[2])
                logger.info(f'Rates added')
            else:
                logger.info(f'ISBN {row[0]} does not exists')
