from db import db


def get_all_topics():
    sql = "SELECT id, name FROM topics ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_topic_name(topic_id):
    sql = "SELECT topics.name FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_topic_difficulty(topic_id):
    sql = "SELECT topics.difficulty FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def create_topic(name):
    sql = "INSERT INTO topics (name, difficulty, question1, question2, question3, question4, question5, answer1, answer2, answer3, answer4, answer5) VALUES (:name, :difficulty, :question1, :question2, :question3, :question4, :question5, :answer1, :answer2, :answer3, :answer4, :answer5) RETURNING id"
    topic_id = db.session.execute(sql, {"name":name, "difficulty":difficulty, "question1":question1, "question2":question2, "question3":question3, "question4":question4, "question5":question5, "answer1":answer1, "answer2":answer2, "answer3":answer3, "answer4":answer4, "answer5":answer5}).fetchone()[0]

def get_question1(topic_id):
    sql = "SELECT topics.question1 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_question2(topic_id):
    sql = "SELECT topics.question2 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_question3(topic_id):
    sql = "SELECT topics.question3 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_question4(topic_id):
    sql = "SELECT topics.question4 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_question5(topic_id):
    sql = "SELECT topics.question5 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_answer1(topic_id):
    sql = "SELECT topics.answer1 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_answer2(topic_id):
    sql = "SELECT topics.answer2 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_answer3(topic_id):
    sql = "SELECT topics.answer3 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_answer4(topic_id):
    sql = "SELECT topics.answer4 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()

def get_answer5(topic_id):
    sql = "SELECT topics.answer5 FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()



