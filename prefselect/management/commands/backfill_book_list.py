import logging
import csv

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from prefselect.models import BannedBook, Author, Genre 

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        BannedBook.objects.all().delete()
        Genre.objects.all().delete()
        Author.objects.all().delete
        with open('banned_books.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                name, authors, ban_year, genre, ban_reason = row
                
                genre, created = Genre.objects.get_or_create(name=genre) 
                book, created = BannedBook.objects.get_or_create(name=name, ban_year=ban_year, ban_reason=ban_reason, genre=genre)
                    
                for author_name in authors.split('and'):
                    author, created = Author.objects.get_or_create(name=author_name)
                    book.authors.add(author)
                
                book.save()

                logger.info(u'Saved Book: {}'.format(book))
