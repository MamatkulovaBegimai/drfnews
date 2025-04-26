from django.shortcuts import render
from rest_framework import viewsets
from news_app.models import News, Comment, Like, Favorite
from news_app.serializers import NewsSerializers, RegisterSerializer, CommentSeralizer, LikeSerializer, FavoriteSerializer
from news_app.permissions import IsAuthorOrReadOnly, IsLikeOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-published_at')
    serializer_class = NewsSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSeralizer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(parent=None).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsLikeOwner]

    def get_queryset(self):
        return Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsLikeOwner]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)