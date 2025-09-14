import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # 1. Query all books by a specific author
    author_name = "John Doe"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        library_books = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in library_books]}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # 3. Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"Librarian of {library.name}: {librarian.name}")
    except Exception:
        print(f"No librarian found for {library_name}")


if __name__ == "__main__":
    run_queries()
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    # --- Create Author ---
    author, created = Author.objects.get_or_create(name="John Doe")

    # --- Create Books ---
    book1, created = Book.objects.get_or_create(title="Book 1", author=author)
    book2, created = Book.objects.get_or_create(title="Book 2", author=author)

    # --- Create Library ---
    library, created = Library.objects.get_or_create(name="Central Library")
    library.books.set([book1, book2])  # Link books to library

    # --- Create Librarian ---
    librarian, created = Librarian.objects.get_or_create(name="Mary", library=library)

    return author, library

def run_queries(author, library):
    # --- Query all books by a specific author ---
    books_by_author = author.books.all()
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # --- Retrieve the librarian for a library ---
    try:
        librarian = library.librarian
        print(f"Librarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library.name}")

if __name__ == "__main__":
    author, library = create_sample_data()
    run_queries(author, library)
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    # --- Create Author ---
    author, created = Author.objects.get_or_create(name="John Doe")

    # --- Create Books ---
    Book.objects.get_or_create(title="Book 1", author=author)
    Book.objects.get_or_create(title="Book 2", author=author)

    # --- Create Library ---
    library, created = Library.objects.get_or_create(name="Central Library")
    books = Book.objects.filter(author=author)
    library.books.set(books)  # Link all books by author to library

    # --- Create Librarian ---
    Librarian.objects.get_or_create(name="Mary", library=library)

    return author, library

def run_queries(author, library):
    # --- Query all books by a specific author using .filter() ---
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # --- Retrieve the librarian for a library ---
    try:
        librarian = library.librarian
        print(f"Librarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library.name}")

if __name__ == "__main__":
    author, library = create_sample_data()
    run_queries(author, library)
python relationship_app/query_samples.py
python relationship_app/query_samples.py
