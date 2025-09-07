files_content = {
    "create.md": """# Create a Book instance

```python
from bookshelf.models import Book

# Create the book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Display the created book
book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>

