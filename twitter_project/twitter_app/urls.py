from django.urls import path
from . import views
from .views import register_view, login_view, tweet_view, delete_tweet_view, logout_view

urlpatterns = [
    path('', views.home, name='home'),  # Defina a view para a URL raiz
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('tweet/', tweet_view, name='tweet'),
    path('tweet/delete/<int:tweet_id>/', delete_tweet_view, name='delete_tweet'),
    path('logout/', logout_view, name='logout'),
]