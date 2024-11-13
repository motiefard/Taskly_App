from rest_framework import routers
from .viewsets import UserViewSet

# app_name = 'users'

router = routers.DefaultRouter()
router.register('user', UserViewSet)