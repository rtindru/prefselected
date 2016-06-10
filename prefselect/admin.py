from django.contrib import admin
from .models import BannedBook, Genre, Author

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BannedBook)
