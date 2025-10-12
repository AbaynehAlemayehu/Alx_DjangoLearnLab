from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='posts-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comments-list-create'),
]
from .views import FeedView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='posts-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comments-list-create'),
    path('feed/', FeedView.as_view(), name='user-feed'),  # ✅ feed endpoint
]
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = router.urls
from django.urls import path
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    # Explicit URLs for likes/unlikes
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
]

# Include router-generated URLs for posts and comments
urlpatterns += router.urls
