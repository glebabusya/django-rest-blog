from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsCurrentUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id
