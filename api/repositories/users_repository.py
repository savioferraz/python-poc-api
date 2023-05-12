from api.database.database import create_connection, close_connection


class UserRepository:
    @staticmethod
    def create_user(name, email):
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO users (name, email) VALUES (?, ?)"
        cursor.execute(query, (name, email))

        close_connection(connection)

    @staticmethod
    def get_user_by_id(user_id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (user_id))
        result = cursor.fetchone()

        close_connection(connection)

        if result is not None:
            return {"name": result[1], "email": result[2]}
        else:
            return None

    @staticmethod
    def get_all_users():
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM users"
        cursor.execute(query)
        results = cursor.fetchall()

        close_connection(connection)

        users = []
        for result in results:
            users.append({"id": result[0], "name": result[1], "email": result[2]})

        return users

    @staticmethod
    def delete_user(user_id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM users WHERE id = ?"
        cursor.execute(query, (user_id,))

        close_connection(connection)
