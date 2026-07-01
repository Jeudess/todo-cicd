from flask import Flask, render_template

from database import configure_database, db
from models import Task

app = Flask(__name__)

configure_database(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():

    tarefas = Task.query.all()

    return render_template(
        "index.html",
        tarefas=tarefas
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)