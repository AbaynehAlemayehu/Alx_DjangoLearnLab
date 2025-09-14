
#### `update.md`:
```md
# Update the Book title

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Expected Output:
# 'Nineteen Eighty-Four'
