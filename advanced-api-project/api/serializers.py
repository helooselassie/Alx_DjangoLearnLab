# BookSerializer: Serializes all fields of the Book model. Includes validation to prevent future publication years.
# AuthorSerializer: Serializes the name field and nests related books dynamically using the BookSerializer.


from rest_framework import serializers
from .models import Author, Book
import datetime
from .models import Book

class BookSerializer(serializers.ModelSerializer):
       class Meta:
           model = Book
           fields = ['title', 'publication_year', 'author']
           fields = '__all__'  # Or list specific fields if necessary

       def validate_publication_year(self, value):
           if value > datetime.date.today().year:
               raise serializers.ValidationError("The publication year cannot be in the future.")
           return value

class AuthorSerializer(serializers.ModelSerializer):
       books = BookSerializer(many=True, read_only=True)

       class Meta:
           model = Author
           fields = ['name', 'books']



        
