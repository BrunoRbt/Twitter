from django.urls import path
from .views import register_view, login_view, tweet_view, delete_tweet_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('tweet/', tweet_view, name='tweet'),
    path('tweet/delete/<int:tweet_id>/', delete_tweet_view, name='delete_tweet'),
]