# relationship_app/forms.py
from django import forms
from .models import Book


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

# In the view:
def search_books(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
