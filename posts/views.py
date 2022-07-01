from webbrowser import get
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.db.models import Count, Q

from rest_framework import generics
from rest_framework.response import Response

from datetime import datetime, time

from .models import Post, LikesOnPosts
from .serializer import PostSerializer, PostCreateSerializer, LikesSerializer, LikesAnalyticsSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostLike(generics.CreateAPIView):
    queryset = LikesOnPosts.objects.all()
    serializer_class = LikesSerializer

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        user = get_object_or_404(get_user_model(), username=request.user)
        try:
            LikesOnPosts.objects.create(user=user, post=post)

        except IntegrityError:
            return Response(status=200, data={'msg': 'Post already liked'})

        post.likes += 1
        post.save()
        return Response(status=201, data={'msg': 'Post liked'})


class PostUnlike(generics.DestroyAPIView):
    queryset = LikesOnPosts.objects.all()
    serializer_class = LikesSerializer

    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        user = get_object_or_404(get_user_model(), username=request.user)
        try:
            obj = LikesOnPosts.objects.get(user=user, post=post)
            obj.delete()
            post.likes -= 1
            post.save()
        except LikesOnPosts.DoesNotExist:
            return Response(status=200, data={'msg': 'Post not liked'})
        return Response(status=204)

class LikesAnalytics(generics.ListAPIView):
    queryset = LikesOnPosts.objects.all()
    serializer_class = LikesAnalyticsSerializer

    def get_queryset(self):
        date_from = datetime.strptime(self.request.GET.get('date_from'), "%Y-%m-%d")
        date_to = datetime.strptime(self.request.GET.get('date_to'), "%Y-%m-%d")
        return LikesOnPosts.objects.annotate(likes=Count('id',
            filter = Q(liked_on__range=(
            datetime.combine(date_from, time.min),
            datetime.combine(date_to, time.max)))))
        