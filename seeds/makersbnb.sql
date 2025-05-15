--Dropping the tables in order
DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;

DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

--creating tables in order
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text,
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,

    price_per_night numeric(10, 2),
    dates_booked DATE ARRAY,
    owner_name text,
    upload_image text

    user_id int,
    constraint fk_spaces foreign key(user_id)
        references users(id)
        on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    request_sender int,
    space_owner int,
    message_content text,
    space_requested int, 
    dates_requested DATE ARRAY,
    accepted boolean,
    constraint fk_request_sender foreign key(request_sender)
        references users(id)
        on delete cascade,
    constraint fk_space_owner foreign key(space_owner)
        references users(id)
        on delete cascade,
    constraint fk_space_owner_requested foreign key(space_requested)
        references spaces(id)
        on delete cascade
);

--Inserting into tables
--users table
-- Inserting into the TABLE

INSERT INTO users (username, email, password) VALUES 
('john_doe', 'johndoe@gmail.com', '$2b$12$R0zBpJO4u/kNrv7jQFavEesRqXKLFiv1fOhiE2Hb71.9YWZLz3EaG'),
('jane_doe', 'janedoe@gmail.com', '$2b$12$aoeO/hoKEgaq2i033emYHOIi.gfKsjUZyDkF25b1PtTeU5.VBaH2.');

--Inserting into the table spaces

INSERT INTO spaces (name, description, price_per_night, dates_booked, user_id, upload_image) VALUES ('Green Lodge', 'A lodge that is green', 100.00, '{[2025-05-20, 2025-05-30]}', 1, 'https://cdn.audleytravel.com/2303/1645/79/492098-phinda-forest-lodge-phinda-private-game-reserve.jpg');
INSERT INTO spaces (name, description, price_per_night, dates_booked, user_id, upload_image) VALUES ('Hobbitsville', 'A place for small people', 200.00, '{[2025-06-01, 2025-06-10]}', 2, 'https://townsquare.media/site/523/files/2023/03/attachment-joshua-harris-9yoPEVoSTcA-unsplash-1.jpg?w=780&q=75');

--Inserting into the table requests
INSERT INTO requests (request_sender, space_owner, message_content, space_requested, dates_requested, accepted)
VALUES
    (1, 2, 'Is this available?', 1, ARRAY['2025-06-15', '2025-06-20']::date[], FALSE),
    (2, 1, 'Is this pet friendly?', 2, ARRAY['2025-07-01', '2025-07-05']::date[], TRUE),
    (1, 1, 'Can I book this?', 1, ARRAY['2025-05-22', '2025-05-24']::date[], FALSE),
    (2, 2, 'Is this kid friendly?', 2, ARRAY['2025-06-10', '2025-06-15']::date[], TRUE);