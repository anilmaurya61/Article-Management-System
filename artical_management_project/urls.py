from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),  # Include the 'users' app URLs
    path('api/', include('articles.urls')), # Include the 'users' app URLs
]
