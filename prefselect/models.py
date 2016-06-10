from __future__ import unicode_literals

from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return '{}'.format(self.name)


class BannedBook(models.Model):
    name = models.CharField(max_length=300)
    genre = models.ForeignKey('Genre', null=True, blank=True, default=None)
    authors = models.ManyToManyField('Author', null=True, blank=True, related_name='banned_books')
    ban_year = models.TextField(null=True, blank=True, default=None)
    ban_reason = models.TextField(null=True, blank=True, default=None)

    def __unicode__(self):
        return '{}'.format(self.name)


class Author(models.Model):
    name = models.CharField(max_length=300)
   
    def __unicode__(self):
        return '{}'.format(self.name)
