from rest_framework import serializers
from .models import Task, TaskList, Attachment
from house.models import House

class TaskListSerializer(serializers.Serializer):
    
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many=False, view_name='house-detail')
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')

    class Meta:
        model = TaskList
        fields = ['url', 'id', 'name', 'description', 'status', 'created_on', 'created_by', 
                  'house', ]
        read_only_fields = ['created_on', 'status', ]


