from rest_framework import permissions


class IsVerifiedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allow read-only access for safe methods (GET, HEAD, OPTIONS)
            return True
        return request.user and request.user.is_verified