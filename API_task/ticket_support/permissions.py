from rest_framework import permissions


class IsOwnerOrAdminOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user or request.user.is_staff)