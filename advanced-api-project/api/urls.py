from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from . import views
from advanced_api_project.views import BookViewSet


urlpatterns = [
       path('books/', BookListView.as_view(), name='book-list'),
       path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
       path('books/create/', BookCreateView.as_view(), name='book-create'),
       path('books/update/', BookUpdateView.as_view(), name='book-update'),
       path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
       path('endpoint/', views.endpoint_view, name='endpoint'),
   ]