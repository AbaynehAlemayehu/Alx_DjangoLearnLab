# advanced_features_and_security/settings.py

# Add your custom user model
AUTH_USER_MODEL = "accounts.CustomUser"

# Make sure you have media settings for profile photos
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
