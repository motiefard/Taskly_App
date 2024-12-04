from rest_framework import permissions

class IsHousemanagerOrNone(permissions.BasePermission):
    """
        custom permission for house-managers to only allow specific privilages for editing 
        specific house attributes.
    """
    
    def has_permission(self, request, view):
        # check is loginned :
        if request.methode in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.methode in permissions.SAFE_METHODS:
            return True
        
        return request.user.profile == obj.manager
        
        
        
        