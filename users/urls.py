from tkinter.font import names

from django.urls import path
from .views import  UserCreateView, UserListView, LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('reset_password', PasswordChangeView.as_view(), name='change-password')
]
