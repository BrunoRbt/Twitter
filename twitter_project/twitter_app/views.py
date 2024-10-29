# views.py
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Tweet, Follow
from .serializers import UserSerializer, TweetSerializer, FollowSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao Twitter Clone!")

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
