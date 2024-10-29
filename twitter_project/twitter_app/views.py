# views.py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Tweet, Follow
from .serializers import UserSerializer, TweetSerializer, FollowSerializer

def home(request):
    return render(request, 'twitter_app/feed.html')

def login_view(request):
    return render(request, 'twitter_app/login.html')

def register_view(request):
    return render(request, 'twitter_app/register.html')

def tweet_view(request):
    return render(request, 'twitter_app/tweet.html')

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    # Implementar lógica de login com JWT
    pass

class FeedView(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        user = self.request.user
        following_users = Follow.objects.filter(follower=user).values_list('following', flat=True)
        return Tweet.objects.filter(user__in=following_users).order_by('-created_at')

class TweetCreateView(generics.CreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class FollowView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
