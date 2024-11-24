from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieves all book instances
    serializer_class = BookSerializer  # Uses the BookSerializer for serialization