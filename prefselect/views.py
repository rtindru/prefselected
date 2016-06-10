from django.shortcuts import get_object_or_404, render, render_to_response

from django.db.models import Prefetch

from .models import *

def books(request, template="books.html"):
    context = {
#        'books': BannedBook.objects.all()
        'books': BannedBook.objects.all().select_related('genre'),
#        'books': BannedBook.objects.all().prefetch_related('genre'),
    }
    return render(request, template, context)

def book_authors(request, template='book_authors.html'):
    context = {
#        'books': BannedBook.objects.all()
#        'books': BannedBook.objects.all().select_related('genre'),
#        'books': BannedBook.objects.all().select_related('genre').prefetch_related('authors'),
    }
    return render(request, template, context)


def ordered_book_authors(request, template='book_authors.html'):
    context = {
#        'books': BannedBook.objects.all().select_related('genre').prefetch_related(
#            Prefetch('authors', queryset=Author.objects.all().order_by('name'))),
#        'books': BannedBook.objects.filter(name__startswith='T').select_related('genre').prefetch_related(
#            Prefetch('authors', queryset=Author.objects.filter(name__startswith='R'))),
    }
    return render(request, template, context)


