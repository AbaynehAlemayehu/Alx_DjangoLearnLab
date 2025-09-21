# bookshelf/forms.py
from django import forms
from .models import Book
from django.core.exceptions import ValidationError
import datetime

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise ValidationError("Title cannot be empty.")
        # Additional sanitization/validation rules can go here
        return title

    def clean_published_date(self):
        date = self.cleaned_data.get("published_date")
        if date and date > datetime.date.today():
            raise ValidationError("Published date cannot be in the future.")
        return date
<!-- bookshelf/templates/bookshelf/form_example.html -->
{% extends "base.html" %}
{% block content %}
  <h2>Create / Edit Book</h2>
  <form method="post" action="{% url 'book_create' %}">
    {% csrf_token %}
    {{ form.non_field_errors }}
    <div>
      <label for="{{ form.title.id_for_label }}">Title</label>
      {{ form.title }}
      {{ form.title.errors }}
    </div>
    <div>
      <label for="{{ form.author.id_for_label }}">Author</label>
      {{ form.author }}
      {{ form.author.errors }}
    </div>
    <div>
      <label for="{{ form.published_date.id_for_label }}">Published date</label>
      {{ form.published_date }}
      {{ form.published_date.errors }}
    </div>

    <button type="submit">Save</button>
  </form>
{% endblock %}
