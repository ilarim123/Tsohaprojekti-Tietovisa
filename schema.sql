CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name TEXT,
    difficulty TEXT,
    question1 TEXT,
    question2 TEXT,
    question3 TEXT,
    question4 TEXT,
    question5 TEXT,
    answer1 TEXT,
    answer2 TEXT,
    answer3 TEXT,
    answer4 TEXT,
    answer5 TEXT
);

CREATE TABLE scoreboard (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    topic_id INTEGER REFERENCES topics,
    score INTEGER
);

