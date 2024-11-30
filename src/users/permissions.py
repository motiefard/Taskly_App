from rest_framework import permissions
# define local permission:

class IsUSerOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
        custom permission for UserViewSet to only allow user to edit their own info, 
        Otherwise Get and Post only.
    """

    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user == obj
        
        return False
    

class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
        custom permission for ProfileViewSet to only allow user to edit their own profile, 
        Otherwise Get and Post only.
    """
     
    def has_permission(self, request, view):
        # return super().has_permission(request, view)
        return True
   
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True    
        
        if not request.user.is_anonymous:
            return request.user.profile == obj
        
        return False
    