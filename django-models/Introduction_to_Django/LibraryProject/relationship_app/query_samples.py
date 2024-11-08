# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (e.g., author with id=1)
author = Author.objects.get(id=1)
books_by_author = Book.objects.filter(author=author)
print("Books by author:", books_by_author)

# List all books in a library (e.g., library with id=1)
library = Library.objects.get(id=1)
books_in_library = library.books.all()
print("Books in library:", books_in_library)

# Retrieve the librarian for a library (e.g., library with id=1)
librarian = Librarian.objects.get(library=library)
print("Librarian for the library:", librarian)
