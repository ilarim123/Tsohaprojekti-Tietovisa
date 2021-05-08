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
            users.add_user_to_scoreboard(username)
            return redirect("/")
        else:
            return render_template("error.html", message="Tapahtui virhe")


@app.route("/select")
def select():
    return render_template("select.html", topics=topics.get_all_topics())


@app.route("/topic/<int:id>")
def topic(id):
    name = topics.get_topic_name(id)
    difficulty = topics.get_topic_difficulty(id)
    questions = topics.get_all_questions(id)

    return render_template("topic.html", id=id, name=name, difficulty=difficulty, questions=questions)

@app.route("/play/<int:id>")
def play(id):
    question = topics.get_question_and_answer(id)[0]
    
    user_id = users.user_id()
    
    return render_template("play.html", id=id, question=question, user_id=user_id)

@app.route("/end/<int:id>", methods=["post"])
def end(id):
    question_id = request.form["question_id"]
    useranswer = request.form["useranswer"]
    user_id = request.form["user_id"]

    result = topics.check_answer(question_id, useranswer, user_id)
    
    if result == True:
        text = "Vastauksesi on oikein! Sait yhden pisteen"
    else:
        text = "Vastauksesi on väärin! Yritä uudestaan"

    return render_template("end.html", id=id, question_id=question_id, user_id=user_id, text=text)

@app.route("/create", methods=["get", "post"])
def create():
    if request.method == "GET":
        return render_template("create.html")

    if request.method == "POST":
        users.check_csrf()

        name = request.form["name"]

        difficulty = request.form["difficulty"]

        topic_id = topics.create_topic(name, difficulty)
        return redirect("/addquestions/"+str(topic_id))

@app.route("/addquestions/<int:id>", methods=["get", "post"])
def addquestions(id):
    if request.method == "GET":
        return render_template("addquestions.html", id=id)
    
    if request.method == "POST":
        users.check_csrf()

        question = request.form["question"]
        
        answer = request.form["answer"]
        
        topic_id = request.form["topic_id"]
        
        topics.add_new_question(topic_id, question, answer)
        return redirect("/addquestions/"+str(topic_id))
        
@app.route("/scoreboard")
def scoreboard():
    return render_template("scoreboard.html", scoreboard=users.get_scoreboard())
