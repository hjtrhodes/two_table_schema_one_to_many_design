-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255),
    post_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title) VALUES ('How to use Git');
INSERT INTO posts (title) VALUES ('Fun classes');
INSERT INTO posts (title) VALUES ('Using a REPL');
INSERT INTO posts (title) VALUES ('A foodie week in Spain');

INSERT INTO comments (content, post_id) VALUES ('Great Stuff!', 4);
INSERT INTO comments (content, post_id) VALUES ('Sick post bruv!', 3);
INSERT INTO comments (content, post_id) VALUES ('Love this!', 2);
INSERT INTO comments (content, post_id) VALUES ('I would actually like to suggest some changes', 3);
INSERT INTO comments (content, post_id) VALUES ('I am a Git pro now!', 1);
INSERT INTO comments (content, post_id) VALUES ('You are da bomb!', 1);
INSERT INTO comments (content, post_id) VALUES ('Holy Moly!', 4);

