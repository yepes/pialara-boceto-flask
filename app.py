from flask import Flask
from flask import render_template


app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world(name='test'):
    return render_template("login.html", name=name)

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/update")
def update():
    return render_template("update.html")


@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/view")
def view():
    return render_template("view.html")
