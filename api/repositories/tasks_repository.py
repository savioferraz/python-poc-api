from api.database.database import create_connection, close_connection


class TaskRepository:
    @staticmethod
    def create_task(user_id, description, created_at):
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO tasks (user_id, description, created_at) VALUES (?, ?, ?)"
        cursor.execute(query, (user_id, description, created_at))

        close_connection(connection)

    @staticmethod
    def get_task_by_id(task_id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM tasks WHERE id = ?"
        cursor.execute(query, (task_id))
        result = cursor.fetchone()

        close_connection(connection)

        if result is not None:
            return {
                "id": result[0],
                "description": result[1],
                "user_id": result[2],
                "created_at": result[3],
            }
        else:
            return None

    @staticmethod
    def get_tasks_by_user(user_id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM tasks WHERE user_id = ?"
        cursor.execute(query, (user_id))
        results = cursor.fetchone()

        close_connection(connection)

        tasks = []
        for result in results:
            tasks.append(
                {
                    "id": result[0],
                    "description": result[1],
                    "user_id": result[2],
                    "created_at": result[3],
                }
            )

        return tasks

    @staticmethod
    def get_all_tasks():
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM tasks"
        cursor.execute(query)
        results = cursor.fetchall()

        close_connection(connection)

        tasks = []
        for result in results:
            tasks.append(
                {
                    "id": result[0],
                    "description": result[1],
                    "user_id": result[2],
                    "created_at": result[3],
                }
            )

        return tasks

    @staticmethod
    def delete_task(task_id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM tasks WHERE id = ?"
        cursor.execute(query, (task_id,))

        close_connection(connection)
