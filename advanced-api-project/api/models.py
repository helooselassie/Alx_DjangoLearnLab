# Author model: Represents an author with a name field. Supports a one-to-many relationship with the Book model.
# Book model: Represents a book with fields for title, publication year, and a foreign key to Author.

from django.db import models

class Author(models.Model):
       name = models.CharField(max_length=255, help_text="Name of the author")

       def __str__(self):
           return self.name

class Book(models.Model):
       title = models.CharField(max_length=255, help_text="Title of the book")
       publication_year = models.IntegerField(help_text="Year of publication")
       author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, help_text="Author of the book")
       

       def __str__(self):
           return self.title