from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include('users.urls')),  # Include the 'users' app URLs
    path('api/', include('articles.urls')), # Include the 'users' app URLs

    # Frontend Pages:
    path('', TemplateView.as_view(template_name='index.html'), name='base'),
    path('login/', TemplateView.as_view(template_name='users/login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='users/register.html'), name='register'),
    path('article/list/', TemplateView.as_view(template_name='articles/list.html'), name='article_list'),
    path('article/create/', TemplateView.as_view(template_name='articles/create.html'), name='article_create'),
    path('article/edit/<int:id>/', TemplateView.as_view(template_name='articles/edit.html'), name='article_edit'),

]
