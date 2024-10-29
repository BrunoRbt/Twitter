from django.urls import path
from .views import register_view, login_view, tweet_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('tweet/', tweet_view, name='tweet'),
]