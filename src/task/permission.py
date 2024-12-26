from rest_framework import permissions

class IsAllowedToEditTaskListElseNone(permissions.BasePermission):
    """
        custom permission for TaskListViewSet to allow the creator editing permission.
    """
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return True
        
        return False


    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.created_by
    


class IsAllowedToEditTaskElseNone(permissions.BasePermission):
    """
        custom permission for TaskViewSet to allow members of a house access to its tasks.
    """

    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.profile.house != None
        
        return False
    
    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task_list.house
    


class IsAllowedToEditAttachmentElseNone(permissions.BasePermission):
    """
        custom permission for AttachmentViewSet to allow members of a house access to its attachment.
    """

    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.profile.house != None
        
        return False
    
    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task.task_list.house