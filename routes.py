from app import app
from flask import render_template, request, redirect
import topics, users

@app.route("/")
def index():
    return render_template("index.html", topics=topics.get_all_topics())

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Virheelliset kirjautumistiedot")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]

    password0 = request.form["password0"]
    if password0 == "":
        return render_template("error.html", message="Syötä jokin salasana")

    if users.register(username, password0):
        return redirect("/")
    else:
        return render_template("error.html", message="Tapahtui virhe")


