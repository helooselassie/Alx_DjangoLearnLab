from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        # Log in the user
        self.client.login(username="testuser", password="testpassword")
        # Create a test book
        self.book = Book.objects.create(title="Test Book", author="Author Test", price=25.0)

    def test_get_books(self):
        # Ensure authenticated user can access the list of books
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        # Test creating a book as an authenticated user
        data = {"title": "New Book", "author": "New Author", "price": 30.0}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "New Book")

    def test_unauthenticated_access(self):
        # Log out the user to test unauthenticated access
        self.client.logout()
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 403)  # Adjust based on your permissions

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create some test data
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2021)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_year=2022)

        # URL endpoints for testing
        self.list_url = '/api/books/'
        self.detail_url = f'/api/books/{self.book1.id}/'

    def test_create_book(self):
        """Test creating a new book via the API."""
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_list_books(self):
        """Test listing all books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        """Test updating an existing book."""
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "publication_year": 2023
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_search_books(self):
        """Test searching for books by title."""
        response = self.client.get(self.list_url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_order_books(self):
        """Test ordering books by publication_year."""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Book One")  # Oldest book first

    def test_permissions(self):
        """Test that permissions are enforced."""
        # Assuming unauthenticated users cannot create books
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "author": "Unauthorized Author",
            "publication_year": 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
