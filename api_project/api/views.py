from rest_framework import generics  # Import generics
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the serializer

class BookList(generics.ListAPIView):  # Extend ListAPIView
    queryset = Book.objects.all()  # Define the queryset
    serializer_class = BookSerializer  # Define the serializer
