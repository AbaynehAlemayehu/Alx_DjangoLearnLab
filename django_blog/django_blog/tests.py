# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def test_signup_creates_user_and_profile(self):
        resp = self.client.post(reverse("blog:signup"), {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "complex_password_123",
            "password2": "complex_password_123",
        })
        # after signup user should exist
        self.assertTrue(User.objects.filter(username="testuser").exists())
        user = User.objects.get(username="testuser")
        # profile should be created via signal
        self.assertIsNotNone(getattr(user, "profile", None))
