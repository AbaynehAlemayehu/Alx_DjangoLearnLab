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
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library   # ✅ Import BOTH Book and Library


# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Required
    context_object_name = 'library'
from django.shortcuts import render
from django.views.generic import DetailView   # ✅ Using DetailView
from .models import Book, Library             # ✅ Import both models


# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-Based View
class LibraryDetailView(DetailView):          # ✅ Class-based view
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Template for CBV
    context_object_name = 'library'

