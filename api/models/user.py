from repositories.users_repository import UserRepository


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        UserRepository.create_user(self.name, self.email)

    @staticmethod
    def get_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    def to_dict(self):
        return {"name": self.name, "email": self.email}