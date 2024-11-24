from rest_framework.generics import ListAPIView
from .models import Book  # Assuming the model name is Book
from .serializers import BookSerializer  # Assuming the serializer is named BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
