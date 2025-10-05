from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import os

def user_avatar_path(instance, filename):
    # uploaded to MEDIA_ROOT/avatars/user_<id>/<filename>
    return f"avatars/user_{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

# Optional: ensure avatar file removed when profile deleted/changed (simple cleanup)
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        # ensure profile exists
        Profile.objects.get_or_create(user=instance)
