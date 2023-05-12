from flask import Blueprint, request, jsonify
from api.controllers.tasks_controllers import (
    create_task,
    get_task,
    get_tasks_by_user,
    get_all_tasks,
    delete_task,
)

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/", methods=["POST"])
def create_task_route():
    data = request.json
    response = create_task(data)
    return jsonify(response)


@tasks_bp.route("/<task_id>", methods=["GET"])
def get_task_route(task_id):
    response = get_task(task_id)
    return jsonify(response)


@tasks_bp.route("/user/<int:user_id>", methods=["GET"])
def get_tasks_by_user_route(user_id):
    response = get_tasks_by_user(user_id)
    return jsonify(response)


@tasks_bp.route("/", methods=["GET"])
def get_all_tasks():
    response = get_all_tasks()
    return jsonify(response)


@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task_route(task_id):
    response = delete_task(task_id)
    return jsonify(response)
