
3. Save the file.  

---

### 4️⃣ Repeat for the other operations

#### `retrieve.md`:
```md
# Retrieve the created Book

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title, book.author, book.publication_year
# Expected Output:
# ('1984', 'George Orwell', 1949)
