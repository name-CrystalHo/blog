from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from django.urls import resolve

# Create your views here.
# def home(request):
#     return render(request,"home.html",{})

class HomeView(ListView):
    model=Post
    template_name="home.html"

    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'
    def get_context_data(self,*args,**kwargs):
        post = get_object_or_404(Post,pk=self.kwargs['pk'])
        photos = PostArticleImage.objects.filter(post=post)

        cat_menu=Category.objects.all()

        context=super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        context["photos"]=photos
        context["cat_menu"]=cat_menu
        return context

def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    cat_menu=Category.objects.all()
    curr_url=request.build_absolute_uri
    about=AboutMe.objects.all()
    return render(request, 'categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts,"cat_menu":cat_menu,"curr_url":curr_url,'about':about})
