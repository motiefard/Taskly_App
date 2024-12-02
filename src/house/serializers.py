from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):

    members_count = serializers.IntegerField(read_only=True)

    class Metta :
        model = House
        fields = ['url', 'id', 'image', 'name', 'create_on', 
                  'manager', 'description', 'members_count', 
                  'members', 'points', 'completed_tasks_count', 
                  'notcompleted_tasks_count', ]
        read_only_fields = ['points', 'completed_tasks_count', 'notcompleted_tasks_count']

