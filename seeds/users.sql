DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text
);

INSERT INTO users (username, email, password) VALUES ('john_doe', 'johndoe@gmail.com', 'password123');
INSERT INTO users (username, email, password) VALUES ('jane_doe', 'janedoe@gmail.com', 'password456');