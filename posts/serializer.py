from dataclasses import field
from rest_framework import serializers

from .models import Post, LikesOnPosts


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'created_at', 'likes',)

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'body',)

class LikesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LikesOnPosts
        fields = ('user', 'post', 'liked_on')

class LikesAnalyticsSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField()
    
    class Meta:
        model = LikesOnPosts
        fields = ('likes',)