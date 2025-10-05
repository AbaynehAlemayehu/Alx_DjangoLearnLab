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
# blog/views.py
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # set the logged-in user as author
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        post_id = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_id)
    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})
