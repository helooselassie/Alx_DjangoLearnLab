# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]


# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Login view with custom template
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout view with custom template
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Register view
    path('register/', views.register, name='register'),
]

