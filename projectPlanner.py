import csv
from collections import namedtuple


Task = namedtuple("Task", ['title', 'duration', 'prerequisites'])


def read_tasks(project):
    tasks = {}
    for row in csv.reader(open(project)):
        number = int(row[0])
        title = row[1]
        duration = float(row[2])
        prerequisites = set(map(int, row[3].split()))
        tasks[number] = Task(title, duration, prerequisites)

    return tasks


def order_tasks():
    incomplete = set(tasks)
    completed = set()
    start_days = {}
    while incomplete:
        for task_number in incomplete:
            task = tasks[task_number]
            if task.prerequisites.issubset(completed):
                earliest_start_day = 0
                for prereq_number in task.prerequisites:
                    prereq_end_day = start_days[prereq_number] + tasks[prereq_number].duration
                    if prereq_end_day > earliest_start_day:
                        earliest_start_day = prereq_end_day
                start_days[task_number] = earliest_start_day
                incomplete.remove(task_number)
                completed.add(task_number)
                break
    return start_days


tasks = read_tasks('project.csv')
print(tasks[3])
