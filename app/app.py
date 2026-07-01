from flask import Flask, render_template, request, redirect

from database import configure_database, db
from models import Task

app = Flask(__name__)

configure_database(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    tarefas = Task.query.order_by(Task.id).all()
    return render_template("index.html", tarefas=tarefas)


@app.route("/add", methods=["POST"])
def add():

    titulo = request.form["title"]

    if titulo.strip():

        nova = Task(title=titulo)

        db.session.add(nova)

        db.session.commit()

    return redirect("/")


@app.route("/complete/<int:id>")
def complete(id):

    tarefa = Task.query.get_or_404(id)

    tarefa.completed = not tarefa.completed

    db.session.commit()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    tarefa = Task.query.get_or_404(id)

    db.session.delete(tarefa)

    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)