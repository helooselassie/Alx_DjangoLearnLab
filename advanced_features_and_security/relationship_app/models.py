from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()  # Ensure this field exists if referenced
    # Other fields...

from django.db import models
from .models import Book  # Make sure to import Book
class Library(models.Model):
    books = models.ManyToManyField(Book)  # Ensure Book is defined correctly
    # Other fields...

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# relationship_app/models.py
from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Other fields...


