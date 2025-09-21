# Permissions and Groups Setup

## Custom Permissions
Defined in `bookshelf/models.py` under the `Book` model:
- can_view → Allows viewing books
- can_create → Allows creating new books
- can_edit → Allows editing existing books
- can_delete → Allows deleting books

## Groups
Configured in Django Admin:
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → can_view, can_create, can_edit, can_delete

## Enforcing Permissions
In `bookshelf/views.py`:
- @permission_required('bookshelf.can_view') → book_list
- @permission_required('bookshelf.can_create') → book_create
- @permission_required('bookshelf.can_edit') → book_edit
- @permission_required('bookshelf.can_delete') → book_delete

## Testing
1. Create users and assign them to groups via Admin.
2. Log in as different users to confirm that permissions are enforced correctly.
