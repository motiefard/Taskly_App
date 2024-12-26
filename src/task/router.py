from rest_framework import routers
from .viewsets import TaskListViewSet

# app_name = 'task'

router = routers.DefaultRouter()
router.register('tasklists', TaskListViewSet)