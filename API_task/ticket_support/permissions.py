from rest_framework import permissions


class IsOwnerOrAdminOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user or request.user.is_staff)


class IsOwnerTicketOrAdminOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return bool(obj.ticket.user == request.user)
