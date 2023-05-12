from flask import Blueprint, request, jsonify
from controllers.users_controllers import create_user, get_user, delete_user

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["POST"])
def create_user_route():
    data = request.get_json()
    response = create_user(data)
    return jsonify(response)


@users_bp.route("/<user_id>", methods=["GET"])
def get_user_route(user_id):
    response = get_user(user_id)
    return jsonify(response)


@users_bp.route("/<user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    response = delete_user(user_id)
    return jsonify(response)
