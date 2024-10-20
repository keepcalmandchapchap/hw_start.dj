from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator
    

class OnlyDelete(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator
    