from django.urls import path
from .views import RegisterView, LoginView, FeedView, TweetCreateView, FollowView, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('tweet/', TweetCreateView.as_view(), name='tweet'),
    path('users/<int:user_id>/follow/', FollowView.as_view(), name='follow'),
]