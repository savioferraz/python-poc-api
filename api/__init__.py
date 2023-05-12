from flask import Blueprint

api_blueprint = Blueprint("api", __name__)

from api.routes.users_routes import *
