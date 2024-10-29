# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Tweet, Follow
from .serializers import UserSerializer, TweetSerializer, FollowSerializer
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'twitter_app/feed.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tweet')
    else:
        form = AuthenticationForm()
    return render(request, 'twitter_app/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro feito com sucesso! Faça login para continuar.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'twitter_app/register.html', {'form': form})

@login_required
def tweet_view(request):
    if request.method == 'POST' and 'content' in request.POST:
        content = request.POST.get('content')
        if content:
            Tweet.objects.create(user=request.user, content=content)
            return redirect('tweet')
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'twitter_app/tweet.html', {'tweets': tweets})

@login_required
def delete_tweet_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet')
    return redirect('tweet')

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
