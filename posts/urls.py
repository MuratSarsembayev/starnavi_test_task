from django.urls import path, re_path
from .views import (PostList, PostCreate, PostDetail, PostLike, PostUnlike, LikesAnalytics)


urlpatterns = [
    path('api/v1/posts/', PostList.as_view()),
    path('api/v1/posts/create/', PostCreate.as_view()),
    path('api/v1/posts/<int:pk>/', PostDetail.as_view()),
    path('api/v1/posts/<int:pk>/like/', PostLike.as_view()),
    path('api/v1/posts/<int:pk>/unlike/', PostUnlike.as_view()),
    re_path(r'api/v1/analytics/$', LikesAnalytics.as_view()),
]
