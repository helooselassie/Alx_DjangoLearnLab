# relationship_app/views.py

from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})
# relationship_app/views.py

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView  # Import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# relationship_app/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Login view (using Django's built-in LoginView)
class UserLoginView(LoginView):
    template_name = 'login.html'

# Logout view (using Django's built-in LogoutView)
class UserLogoutView(LogoutView):
    template_name = 'logout.html'

# Register view (using Django's built-in UserCreationForm)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

