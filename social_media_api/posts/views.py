from rest_framework import generics, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    """
    Returns posts from users that the current user follows, ordered by creation date (newest first).
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the users that the current user is following
        following_users = self.request.user.following.all()
        # Return posts from those users, newest first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD for posts
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD for comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Like
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Create a notification
            from notifications.models import Notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'status': 'post liked'})
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'post unliked'})
        except Like.DoesNotExist:
            return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status, permissions, viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Like
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        # ✅ use generics.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            from notifications.models import Notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'status': 'post liked'})
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'post unliked'})
        except Like.DoesNotExist:
            return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
