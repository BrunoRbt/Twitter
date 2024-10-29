from django.urls import path
from .views import RegisterView, LoginView, FeedView, TweetCreateView, FollowView, home, login_view, register_view, tweet_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('tweet/', tweet_view, name='tweet'),
    path('users/<int:user_id>/follow/', FollowView.as_view(), name='follow'),
]