from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # optionally activate or send email verification here
            auth_login(request, user)  # log the user in immediately after signup
            messages.success(request, "Signup successful. Welcome, %s!" % user.username)
            return redirect("blog:post_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def profile_view(request, username=None):
    # if username provided view that user's profile, else current user
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
    profile = getattr(user, "profile", None)
    return render(request, "blog/profile.html", {"profile_user": user, "profile": profile})

@login_required
def profile_edit(request):
    if request.method == "POST":
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect("blog:profile")  # redirect to own profile
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "blog/profile_edit.html", {"uform": uform, "pform": pform})
