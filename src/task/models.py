from django.db import models


NOT_COMPLETE = 'NC'
COMPLETED = 'C'
TASK_STATUS_CHOICES = [
    (NOT_COMPLETE,  'Not Completed'),
    (COMPLETED,  'Completed')
]


class Task(models.Model):
    creared_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        'users.Profile', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_tasks')
    completed_by = models.ForeignKey(
        'users.Profile', on_delete=models.SET_NULL, null=True, blank=True, related_name='completed_tasks')
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=TASK_STATUS_CHOICES,
        default=NOT_COMPLETE
    )


    def __str__(self):
        return f'{self.id} | {self.name}'
