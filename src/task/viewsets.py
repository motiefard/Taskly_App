from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, response, status, filters
from rest_framework.decorators import action
from .models import TaskList, Task, Attachment
from .models import COMPLETED, NOT_COMPLETE
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer
from .permission import IsAllowedToEditTaskListElseNone, IsAllowedToEditTaskElseNone, IsAllowedToEditAttachmentElseNone

class TaskListViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                      #mixins.ListModelMixin, 
                      viewsets.GenericViewSet):
    permission_classes = [IsAllowedToEditTaskListElseNone, ]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAllowedToEditTaskElseNone, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ['status', ]
    search_fields = ['name', 'description']
    
    def get_queryset(self):
        queryset =  super(TaskViewSet, self).get_queryset()
        user_profile = self.request.user.profile
        updated_queryset = queryset.filter(created_by = user_profile)
        return updated_queryset
    
    @action(detail=True, methods=['patch'])
    def update_task_status(self, request, pk=None):
        try:
            task = self.get_object()
            req_profile = request.user.profile
            req_status = request.data['status']
            if req_status == NOT_COMPLETE :
                if task.status == COMPLETED :
                    task.status = NOT_COMPLETE
                    task.completed_on = None
                    task.completed_by = None    
                else:
                    raise Exception("Task is already mark as not complete.")
            elif req_status == COMPLETED :
                if task.status == NOT_COMPLETE :
                    task.status = COMPLETED
                    task.completed_on = timezone.now()
                    task.completed_bby = req_profile
                else:
                    raise Exception("Task is already mark as complete.")
            else:
                raise Exception("Incorrect status provided.")
            task.save()
            serilizer = TaskSerializer(instance=task, context={'request':request})
            return response.Response(serilizer.data, status=status.HTTP_200_OK)

        except Exception as err:
            return response.Response({'detail':str(err)}, status=status.HTTP_400_BAD_REQUEST)


class AttachmentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                      #mixins.ListModelMixin, 
                      viewsets.GenericViewSet):
    permission_class = [IsAllowedToEditAttachmentElseNone, ]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer