from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class LikesOnPosts(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}:{self.post}'
    
    class Meta:
        unique_together = ['user', 'post']
