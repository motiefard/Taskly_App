from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import House
from .serializers import HouseSerializer
from .permissions import IsHousemanagerOrNone

class HouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsHousemanagerOrNone, ]
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    @action(detail=True, methods=['post'], name='join', permission_classes=[])
    def join(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.profile
            if(user_profile.house == None):
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            elif(user_profile in house.members.all()):
                return Response({'detail': 'Already a member in this house.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={'detail': 'Already a member in another house.', 
                                #  'user':str(request.user.username), 
                                #  'this_house':str(house.name), 
                                #  'own_house':str(user_profile.house.name)
                                 }, 
                                 status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response(data={ "message": "my msg.", "error": str(err)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    @action(detail=True, methods=['post'], name='leave', permission_classes=[])
    def leave(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.profile
            if(user_profile in house.members.all()):
                user_profile.house = None
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'detail': 'user not a member in this house.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)