from api.repositories.users_repository import UserRepository


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        UserRepository.create_user(self.name, self.email)

    @staticmethod
    def get_by_id(user_id):
        user_dict = UserRepository.get_user_by_id(user_id)
        if user_dict:
            return User(user_id, user_dict["name"], user_dict["email"])
        else:
            return None

    @staticmethod
    def get_all():
        user_dicts = UserRepository.get_all_users()
        users = [
            User(user_dict["id"], user_dict["name"], user_dict["email"])
            for user_dict in user_dicts
        ]

        return users

    def delete(self):
        UserRepository.delete_user(self.id)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}
