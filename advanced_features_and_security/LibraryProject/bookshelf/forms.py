# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book
from django.core.exceptions import ValidationError
import datetime

class BookForm(forms.ModelForm):
    """Form for creating and editing Book objects with validation."""
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise ValidationError("Title cannot be empty.")
        return title

    def clean_published_date(self):
        date = self.cleaned_data.get("published_date")
        if date and date > datetime.date.today():
            raise ValidationError("Published date cannot be in the future.")
        return date


class ExampleForm(forms.Form):
    """A simple example form for demonstration and testing security features."""
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not name:
            raise ValidationError("Name cannot be blank
