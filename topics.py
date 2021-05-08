from db import db


def get_all_topics():
    sql = "SELECT id, name FROM topics ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_topic_name(topic_id):
    sql = "SELECT topics.name FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()[0]

def get_topic_difficulty(topic_id):
    sql = "SELECT topics.difficulty FROM topics WHERE topics.id=:topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()[0]

def get_topic_question_amount(topic_id):
    sql = "SELECT COUNT(*) FROM questions WHERE topic_id = :topic_id"
    return db.session.execute(sql, {"topic_id": topic_id}).fetchone()[0]

def create_topic(name, difficulty):
    sql = "INSERT INTO topics (name, difficulty) VALUES (:name, :difficulty) RETURNING id"
    topic_id = db.session.execute(sql, {"name":name, "difficulty":difficulty}).fetchone()[0]
    
    db.session.commit()
    return topic_id

def add_new_question(topic_id, question, answer):
    sql = "INSERT INTO questions (topic_id, question, answer) VALUES (:topic_id, :question, :answer)"
    db.session.execute(sql, {"topic_id":topic_id, "question":question, "answer":answer})
    db.session.commit()

def get_next_question(topic_id, qnumber):
    sql = "SELECT id, question FROM questions WHERE topic_id=:topic_id LIMIT 1 OFFSET :qnumber"
    return db.session.execute(sql, {"topic_id":topic_id, "qnumber":qnumber}).fetchone()
    
def get_all_questions(topic_id):
    sql = "SELECT id, question FROM questions WHERE topic_id=:topic_id"
    return db.session.execute(sql, {"topic_id":topic_id}).fetchall()

def get_question_and_answer(question_id):
    sql = "SELECT question, answer FROM questions WHERE id=:question_id"
    return db.session.execute(sql, {"question_id":question_id}).fetchone()
    
def check_answer(question_id, useranswer, user_id):
    sql = "SELECT answer FROM questions WHERE id=:question_id"
    correct = db.session.execute(sql, {"question_id":question_id}).fetchone()[0]
    
    if useranswer == correct:
        points = 1
        right = True
    else:
        points = 0
        right = False
    
    sql = "UPDATE scoreboard SET score=score+:points WHERE id=:user_id"
    
    db.session.execute(sql, {"user_id":user_id, "question_id":question_id, "points":points})
    db.session.commit()
    return right
