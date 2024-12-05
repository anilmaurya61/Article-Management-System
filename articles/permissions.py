from rest_framework.permissions import BasePermission

class IsJournalist(BasePermission):
    """
    Allows access only to journalists who created the article.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action in ['update', 'destroy'] and request.user == view.get_object().author:
                return True
            return False
        return False


class IsEditorOrAdmin(BasePermission):
    """
    Allows access to editors and admins to approve, reject, or publish articles.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.role == 'editor' or request.user.role == 'admin')
