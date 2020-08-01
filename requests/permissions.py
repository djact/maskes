from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `requester`.
        return obj.requester == request.user

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return obj.requester == request.user

class IsVolunteerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_volunteer
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_volunteer