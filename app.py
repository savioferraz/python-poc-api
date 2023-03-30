from flask import Flask

app = Flask(__name__)


@app.route("/")
def teste():
    return "Funcionando"


if __name__ == "__main__":
    app.run(debug=True)
