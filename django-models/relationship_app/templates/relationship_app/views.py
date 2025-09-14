# relationship_app/views.py
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
from django.shortcuts import render

# Create your views here.
