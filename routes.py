from app import app
from flask import render_template, request, redirect
import topics, users

@app.route("/")
def index():
    return render_template("index.html")

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


@app.route("/select")
def select():
    return render_template("select.html", topics=topics.get_all_topics())


@app.route("/topic/<int:id>")
def topic(id):
    name = topics.get_topic_name(id)
    desc = topics.get_topic_desc(id)
    difficulty = topics.get_topic_difficulty(id)
    question1 = topics.get_question1(id)
    question2 = topics.get_question2(id)
    question3 = topics.get_question3(id)
    question4 = topics.get_question4(id)
    question5 = topics.get_question5(id)
    answer1 = topics.get_answer1(id)
    answer2 = topics.get_answer2(id)
    answer3 = topics.get_answer3(id)
    answer4 = topics.get_answer4(id)
    answer5 = topics.get_answer5(id)

    return render_template("topic.html", id=id, name=name, desc=desc, difficulty=difficulty, question1=question1, question2=question2, question3=question3, question4=question4, question5=question5, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5)

@app.route("/create", methods=["get", "post"])
def create():
    if request.method == "GET":
        return render_template("create.html")

    if request.method == "POST":
        users.check_csrf()

        name = request.form["name"]

        difficulty = request.form["difficulty"]

        if difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != "4" and difficulty != "5":
            return render_template("error.html", message="Vaikeusasteen tulee olla kokonaisluku väliltä 1-5")


        question1 = request.form["question1"]
        question2 = request.form["question2"]
        question3 = request.form["question3"]
        question4 = request.form["question4"]
        question5 = request.form["question5"]
        answer1 = request.form["answer1"]
        answer2 = request.form["answer2"]
        answer3 = request.form["answer3"]
        answer4 = request.form["answer4"]
        answer5 = request.form["answer5"]

        topic_id = topics.create_topic(name, difficulty, question1, question2, question3, question4, question5, answer1, answer2, answer3, answer4, answer5)
        return redirect("/topic/"+str(topic_id))


