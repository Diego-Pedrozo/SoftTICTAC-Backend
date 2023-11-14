from rest_framework import permissions
from apps.user.choices import UserRanges

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user_type = request.user.information.user_type
        
        if user_type == UserRanges.ADMIN:
            return True
        return False