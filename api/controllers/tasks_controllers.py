from api.models.task import Task
import datetime


def create_task(data):
    user_id = data.get("user_id")
    description = data.get("description")
    created_at = datetime.datetime.now()

    new_task = Task(None, user_id, description, created_at)
    new_task.save()

    return {"message": "Task created successfully", "task": new_task.to_dict()}


def get_task(task_id):
    task = Task.get_by_id(task_id)
    if task:
        return task.to_dict()
    else:
        return {"message": "Task not found"}


def get_tasks_by_user(user_id):
    tasks = Task.get_by_user(user_id)
    tasks_dicts = [task.to_dict() for task in tasks]
    return tasks_dicts


def get_all_tasks():
    tasks = Task.get_all()
    tasks_dicts = [task.to_dict() for task in tasks]
    return tasks_dicts


def delete_task(task_id):
    task = Task.get_by_id(task_id)

    if task:
        task.delete()
        return {"message": "Task deleted successfully"}
    else:
        return {"message": "Task not found"}
