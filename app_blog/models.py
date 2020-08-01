from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name="Add a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="what is on your mind?")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name="Blog Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    """
    class Meta:
        ordering = ['-publish_date'] #another way of oredring by objects instead of queryset
    """
    
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField(verbose_name="Type Your Comment:")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-comment_date']
    
    def __str__(self):
        return self.comment
class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='liked_user')
    
    def __str__(self):
        return self.user + 'Likes' + self.blog
    
     