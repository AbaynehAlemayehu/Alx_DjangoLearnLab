# blog/admin.py
from django.contrib import admin
from .models import Post, Comment, Profile

admin.site.register(Profile)

# keep existing Post and Comment registration (if present)
from django.contrib import admin

# Register your models here.
