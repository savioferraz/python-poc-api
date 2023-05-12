from api.models.user import User


def create_user(data):
    name = data.get("name")
    email = data.get("email")

    new_user = User(name, email)
    new_user.save()

    return {"message": "User created successfully", "user": new_user.to_dict()}


def get_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        return user.to_dict()
    else:
        return {"message": "User not found"}


def get_all_users():
    users = User.get_all()
    users_dicts = [user.to_dict() for user in users]
    return users_dicts


def delete_user(user_id):
    user = User.get_by_id(user_id)

    if user:
        user.delete()
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}
