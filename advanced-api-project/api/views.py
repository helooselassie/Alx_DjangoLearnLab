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
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework
from .filters import BookFilter
from rest_framework.filters import OrderingFilter
from rest_framework import filters
from rest_framework import filters, generics


class BookListView(generics.ListAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_classes = [AllowAny]
       filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Include both filters
       search_fields = ['title', 'author__name']  # Fields to search
       ordering_fields = ['title', 'publication_year']  # Specify fields that can be used for ordering
       ordering = ['title']  # Set a default ordering

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

import django_filters

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    publication_year = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # Add OrderingFilter here
    filterset_class = BookFilter  # Use your custom filter class
    search_fields = ['title', 'author']  # Fields to search
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering by title
