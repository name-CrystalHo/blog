from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=255)
   # author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=255,default='fun')
    cover_image=models.ImageField(null=True, blank=True, upload_to="images/")
    article_image=models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.title +' | '+ str(self.category)