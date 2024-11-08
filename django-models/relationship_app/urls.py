# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView  # Import list_books and LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL pattern for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view
]


# relationship_app/urls.py
from django.urls import path
from .views import UserLoginView, UserLogoutView, register

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),  # Register URL
]

