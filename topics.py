from db import db
from random import randint

def get_all_topics():
    sql = "SELECT id, name FROM topics ORDER BY name"
    return db.session.execute(sql).fetchall()

def create_topic(name):
    pass


