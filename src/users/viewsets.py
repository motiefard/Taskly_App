from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from .serializers import UserSerializer, ProfileSerializer
from .permissions import IsUSerOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly
from .models import Profile

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUSerOwnerOrGetAndPostOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = [IsProfileOwnerOrReadOnly, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer