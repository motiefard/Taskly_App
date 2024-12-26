from rest_framework import viewsets, mixins
from .models import TaskList, Task, Attachment
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer
from .permission import IsAllowedToEditTaskListElseNone, IsAllowedToEditTaskElseNone, IsAllowedToEditAttachmentElseNone

class TaskListViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAllowedToEditTaskListElseNone, ]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAllowedToEditTaskElseNone, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AttachmentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_class = [IsAllowedToEditAttachmentElseNone, ]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer