from rest_framework.permissions import BasePermission

SAFE_METHODS = ['GET']

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

        
