from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(AboutMe)
class PostImageAdmin(admin.StackedInline):
    model = PostArticleImage
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Post
 
@admin.register(PostArticleImage)
class PostImageAdmin(admin.ModelAdmin):
    pass