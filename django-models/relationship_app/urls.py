# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView  # Import list_books and LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL pattern for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view
]


# relationship_app/urls.py

from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView  # Import your views

urlpatterns = [
    path('login/', UserLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/', register, name='register')
]

