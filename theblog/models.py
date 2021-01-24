from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=255)
    category=models.CharField(max_length=255,default='fun')
    cover_image=models.ImageField(null=True, blank=True, upload_to="images/")
    article_image=models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.title +' | '+ str(self.category)

class PostArticleImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title

class AboutMe(models.Model):
    description= models.CharField(max_length=2000)
    picture=models.ImageField(null=True, blank=True, upload_to="images/")
