
#### `delete.md`:
```md
# Delete the Book

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()
Book.objects.all()
# Expected Output:
# <QuerySet []>
