from django.urls import path
from setuptools.extern import names

from .views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticlePublishView, ArticleDeleteView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/create/', ArticleCreateView.as_view(), name='article-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:pk>/', ArticlePublishView.as_view(), name='update-status'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete-article')
]
