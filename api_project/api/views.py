from rest_framework import viewsets
from rest_framework import generics  # Import generics
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the serializer
from rest_framework.permissions import IsAuthenticated


class BookList(generics.ListAPIView):  # Extend ListAPIView
    queryset = Book.objects.all()  # Define the queryset
    serializer_class = BookSerializer  # Define the serializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Use the Book serializer
    permission_classes = [IsAuthenticated] 