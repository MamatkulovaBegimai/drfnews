from django.shortcuts import render
from rest_framework import viewsets
from news_app.models import News
from news_app.serializers import NewsSerializers
# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-published_at')
    serializer_class = NewsSerializers

