from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=255)
    category=models.CharField(max_length=255,default='fun')
    cover_image=models.ImageField(null=True, blank=True, upload_to="images/")
    article_image=models.ImageField(null=True, blank=True, upload_to="images/")
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    def __str__(self):
        return self.title +' | '+ str(self.category)
    class Meta:
        ordering = ['-date',]

class PostArticleImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title

class AboutMe(models.Model):
    description= RichTextField(blank=True,null=True)
    picture=models.ImageField(null=True, blank=True, upload_to="images/")
    resume=models.FileField(null=True, blank=True, upload_to="images/")
