# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView  # Import list_books and LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL pattern for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view
]
