from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import House
from .serializers import HouseSerializer
from .permissions import IsHousemanagerOrNone

class HouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsHousemanagerOrNone, ]
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['members',]
    search_fields = ['name', '=description']
    ordering_fields = ['points', 'completed_tasks_count', 'notcompleted_tasks_count']

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
        
    
    @action(detail=True, methods=['post'], name='remove member', permission_classes=[])
    def remove_member(self, request, pk=None):
        try:
            house = self.get_object()
            user_id = request.data.get('user_id', None)
            if(user_id == None):
                return Response({'user_id':'Not provided.'}, status=status.HTTP_400_BAD_REQUEST)
            user_profile = User.objects.get(pk=user_id).profile
            
            house_members = house.members
            if(user_profile in house_members.all()):
                house_members.remove(user_profile)
                house.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'detail':'User not a member in this house.'}, status=status.HTTP_400_BAD_REQUEST)

            # if(user_profile.house == house):
            #     user_profile.house = None
            #     user_profile.save()
            #     return Response(status=status.HTTP_204_NO_CONTENT)
            # else:
            #     return Response({'detail':'User not a member in this house.'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response({'detail':'Provided user_id does not exist.'}, status=status.HTTP_400_BAD_REQUEST)