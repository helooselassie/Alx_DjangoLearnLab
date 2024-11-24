from rest_framework import generics
from .models import Book  # Adjust to match your model name
from .serializers import BookSerializer  # Ensure this matches your serializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
