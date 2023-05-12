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
        result = cursor.execute(query, (user_id))

        close_connection(connection)

        if result:
            return {"name": result[1], "email": result[2]}
        else:
            return None

    @staticmethod
    def delete_user(user_id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM users WHERE id = ?"
        cursor.execute(query, (user_id,))

        close_connection(connection)
