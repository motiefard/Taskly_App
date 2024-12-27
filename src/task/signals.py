from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Task, TaskList, COMPLETED, NOT_COMPLETE

@receiver(post_save, sender=Task)
def update_tasklist_status(sender, instance, created, **kwaurgs):
    tasklist = instance.task_list
    is_compelete = True
    for task in tasklist.tasks.all():
        if task.status != COMPLETED :
            is_compelete = False
            break
    
    tasklist.status = COMPLETED if is_compelete else NOT_COMPLETE
    tasklist.save()


@receiver(post_save, sender=Task)
def update_house_point(sender, instance, created, **kwaurgs):
    house = instance.task_list.house
    if instance.status == COMPLETED:
        house.points += 10
    elif instance.status == NOT_COMPLETE:
        if house.points >= 10 :
            house.points -=10
    house.save()