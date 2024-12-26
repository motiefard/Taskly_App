from rest_framework import viewsets, mixins
from .models import TaskList, Task, Attachment
from .serializers import TaskListSerializer
from .permission import IsAllowedToEditTaskListElseNone

class TaskListViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAllowedToEditTaskListElseNone, ]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

