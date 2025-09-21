# advanced_features_and_security/settings.py

# Add your custom user model
AUTH_USER_MODEL = "accounts.CustomUser"

# Make sure you have media settings for profile photos
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
# settings.py

AUTH_USER_MODEL = "bookshelf.CustomUser"
# LibraryProject/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: set to False in production (True only for local dev)
DEBUG = False

# Replace with your actual domain names in production
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com", "localhost", "127.0.0.1"]

# ----- Security-related settings -----
# Prevent clickjacking
X_FRAME_OPTIONS = "DENY"  # or "SAMEORIGIN" if you need frames from same origin

# Enable browser XSS filter header
SECURE_BROWSER_XSS_FILTER = True

# Disable content type sniffing by browsers
SECURE_CONTENT_TYPE_NOSNIFF = True

# Use HTTPS-only cookies in production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Ensure cookies are not accessible via JavaScript
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False  # usually False so your front-end frameworks can read CSRF if needed

# Force HTTPS redirect (only if you have HTTPS configured)
SECURE_SSL_REDIRECT = True

# HSTS (HTTP Strict Transport Security). Only enable when HTTPS is working.
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Content Security Policy: optionally handled by middleware or django-csp
# If you use django-csp, configure CSP_* settings; otherwise use custom middleware.
# Example placeholder (if you use django-csp):
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", "https://trusted-cdn.example.com")

# ----- Middleware: ensure SecurityMiddleware is present -----
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # If using custom CSP middleware, add it after SecurityMiddleware:
    "libraryproject.security.middleware.ContentSecurityPolicyMiddleware",  # sample path if using manual
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # ... other middleware
]

# Note: Adjust INSTALLED_APPS/MIDDLEWARE ordering if necessary.
