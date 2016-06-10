import logging
import csv

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from prefselect.models import BannedBook, Author, Genre 

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        book_list = list(BannedBook.objects.all())
        for book in book_list:
            b = BannedBook.objects.create(name=book.name, genre=book.genre, ban_year=book.ban_year, ban_reason=book.ban_reason)
            for author in book.authors.all():
                b.authors.add(author)
            b.save()

