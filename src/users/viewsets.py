from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsUSerOwnerOrGetAndPostOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUSerOwnerOrGetAndPostOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer