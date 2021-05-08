CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name TEXT,
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
    username TEXT,
    score INTEGER
);
