   # BookListView: Handles retrieving all books (read-only, public access).
   # BookDetailView: Handles retrieving a specific book by ID (read-only, public access).
   # BookCreateView: Handles creating a new book (restricted to authenticated users).
   # BookUpdateView: Handles updating an existing book (restricted to authenticated users).
   # BookDeleteView: Handles deleting a book (restricted to authenticated users).


from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookListView(generics.ListAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_classes = [AllowAny]

class BookDetailView(generics.RetrieveAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_classes = [AllowAny]

class BookCreateView(generics.CreateAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_classes = [IsAuthenticatedOrReadOnly]