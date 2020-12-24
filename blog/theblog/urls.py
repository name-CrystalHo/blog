from django.urls import path
from .views import HomeView,ArticleDetailView,CategoryView
from .models import Category

urlpatterns = [
  path('',HomeView.as_view(),name="home"),
  path('article/<int:pk>',ArticleDetailView.as_view(),name="article-detail"),
  path('category/<str:cats>/',CategoryView, name='category'),
]

