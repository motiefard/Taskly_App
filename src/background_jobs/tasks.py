from background_task import background
from background_task.tasks import Task as BT

from house.models import House
from task.models import COMPLETED

@background(schedule=10)
def calculate_house_stats():
    for house in House.objects.all():
        total_tasks = 0
        compeleted_task_count = 0
        house_task_lists = house.tasklists.all()
        for task_list in house_task_lists:
            total_tasks += task_list.tasks.count()
            compeleted_task_count += task_list.tasks.filter(status=COMPLETED).count()
        
        house.completed_tasks_count = compeleted_task_count
        house.notcompleted_tasks_count = total_tasks - compeleted_task_count
        house.save()


if not BT.objects.filter(verbose_name='calculate_house_stats').exists():
    calculate_house_stats(repeat=BT.DAILY, verbose_name='calculate_house_stats', priority=0)