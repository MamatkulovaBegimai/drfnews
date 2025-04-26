# serializers.py
from rest_framework import serializers
from news_app.models import News, Comment, Like, Favorite
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


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSeralizer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    replies = RecursiveField(many=True, read_only=True)
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Comment
        fields = ['id', 'news', 'text', 'author', 'created_at', 'parent', 'replies']


class NewsSerializers(serializers.ModelSerializer):
    comments = CommentSeralizer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'published_at', 'author', 'comments', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['user']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ['user']


