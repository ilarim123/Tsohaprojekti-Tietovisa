CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name TEXT
    desc TEXT
    difficulty TEXT
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics,
    question TEXT,
    answer TEXT
);

CREATE TABLE scoreboard (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    topic_id INTEGER REFERENCES topics
    score INTEGER
);

