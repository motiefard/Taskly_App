from rest_framework import viewsets
from .models import House
from .serializers import HouseSerializer
from .permissions import IsHousemanagerOrNone

class HouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsHousemanagerOrNone, ]
    queryset = House.objects.all()
    serializer_class = HouseSerializer