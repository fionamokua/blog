from rest_framework import permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #read permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        #writepermission
        return obj.author == request.user