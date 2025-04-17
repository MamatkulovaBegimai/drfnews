# serializers.py
from rest_framework import serializers
from news_app.models import News, Comment
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class CommentSeralizer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'news', 'text', 'author', 'created_at']


class NewsSerializers(serializers.ModelSerializer):
    comments = CommentSeralizer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'published_at', 'author', 'comments']

