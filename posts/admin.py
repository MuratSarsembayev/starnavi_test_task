from django.contrib import admin

from .models import Post, LikesOnPosts


admin.site.register(Post)
admin.site.register(LikesOnPosts)
