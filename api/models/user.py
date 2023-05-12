from api.repositories.users_repository import UserRepository


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        UserRepository.create_user(self.name, self.email)

    @staticmethod
    def get_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def get_all():
        return UserRepository.get_all_users()

    @staticmethod
    def delete(user_id):
        UserRepository.delete_user(user_id)

    def to_dict(self):
        return {"name": self.name, "email": self.email}
