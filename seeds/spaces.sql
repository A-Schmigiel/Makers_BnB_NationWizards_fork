DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price_per_night numeric(10, 2),
    dates_available DATE ARRAY,
    user_id int,
    constraint fk_spaces foreign key(user_id)
        references users(id)
        on delete cascade
);

INSERT INTO spaces (name, description, price_per_night, dates_available, user_id) VALUES ('Green Lodge', 'A lodge that is green', 100.00, '{[2025-05-20, 2025-05-30]}', 1);
INSERT INTO spaces (name, description, price_per_night, dates_available, user_id) VALUES ('Hobbitsville', 'A place for small people', 200.00, '{[2025-06-01, 2025-06-10]}', 2);