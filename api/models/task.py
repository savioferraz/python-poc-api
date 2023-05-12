from api.repositories.tasks_repository import TaskRepository


class Task:
    def __init__(self, id, user_id, description, created_at):
        self.id = id
        self.user_id = user_id
        self.description = description
        self.created_at = created_at

    def save(self):
        TaskRepository.create_task(self.user_id, self.description, self.created_at)

    @staticmethod
    def get_by_id(task_id):
        task_dict = TaskRepository.get_task_by_id(task_id)

        if task_dict:
            return Task(
                task_dict["id"],
                task_dict["description"],
                task_dict["user_id"],
                task_dict["created_at"],
            )
        else:
            return None

    @staticmethod
    def get_by_user(user_id):
        return TaskRepository.get_tasks_by_user(user_id)

    @staticmethod
    def get_all():
        task_dicts = TaskRepository.get_all_tasks()
        tasks = [
            Task(
                task_dict["id"],
                task_dict["description"],
                task_dict["user_id"],
                task_dict["created_at"],
            )
            for task_dict in task_dicts
        ]

        return tasks

    def delete(self):
        TaskRepository.delete_task(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "user_id": self.user_id,
            "created_at": self.created_at,
        }
