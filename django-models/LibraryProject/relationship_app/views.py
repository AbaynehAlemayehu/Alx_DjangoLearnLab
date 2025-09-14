from django.shortcuts import render
# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

# Create your views here.
    from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

