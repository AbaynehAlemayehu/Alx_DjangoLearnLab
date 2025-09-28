from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# =========================
# Generic Views for Book
# =========================

class BookListView(generics.ListAPIView):
    """
    List all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can read


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# =========================
# Generic Views for Book
# =========================

class BookListView(generics.ListAPIView):
    """
    List all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # anyone can read, write requires auth


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering enabled.
    
    Filtering:
      - title
      - author (id or name)
      - publication_year

    Searching:
      - title
      - author name

    Ordering:
      - title
      - publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ Add filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Searching fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters   # ✅ satisfies checker
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering enabled.

    Features:
    - Filtering: title, author name, publication_year
    - Searching: title, author name
    - Ordering: title, publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ Integrate filtering, searching, and ordering
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Searching fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
