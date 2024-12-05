from rest_framework.permissions import BasePermission

class IsJournalist(BasePermission):
    """
    Custom permission to allow only journalists to create and edit their own articles.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'journalist'


class IsEditor(BasePermission):
    """
    Custom permission to allow only editors to approve, reject, or publish articles.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'editor'


class IsAdmin(BasePermission):
    """
    Custom permission to allow only admins to manage articles.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
