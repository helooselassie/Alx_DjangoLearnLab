# LibraryProject/bookshelf/admin.py

from django.contrib import admin
from .models import Library, Book

admin.site.register(Library)
admin.site.register(Book)
