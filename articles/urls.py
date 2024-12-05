from django.urls import path
from .views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticlePublishView, ArticleApproveView, ArticleRejectView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/create/', ArticleCreateView.as_view(), name='article-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:pk>/publish/', ArticlePublishView.as_view(), name='article-publish'),
    path('articles/<int:pk>/approve/', ArticleApproveView.as_view(), name='article-approve'),
    path('articles/<int:pk>/reject/', ArticleRejectView.as_view(), name='article-reject'),
]
