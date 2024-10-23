# twitter_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TweetViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'tweets', TweetViewSet)
router.register(r'follows', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]