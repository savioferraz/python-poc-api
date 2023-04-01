from flask import Flask, request, jsonify

app = Flask(__name__)

db = []


@app.route("/test", methods=["GET"])
def teste():
    return "Funcionando"


@app.route("/tasks", methods=["POST"])
def create_task():
    task = request.json
    db.append(task)
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    return jsonify(db), 200


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    return jsonify(db[id]), 200


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = request.json
    db[id] = task
    return jsonify(db[id]), 201


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    del db[id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
