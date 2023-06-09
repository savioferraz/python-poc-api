from flask import Flask
from api.database.database import create_tables
from api.routes.users_routes import users_bp
from api.routes.tasks_routes import tasks_bp

app = Flask(__name__)

app.config["DATABASE"] = "api/database/database.db"


@app.before_first_request
def initialize_database():
    create_tables()


@app.route("/health")
def health():
    return "Server running"


app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(tasks_bp, url_prefix="/tasks")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
