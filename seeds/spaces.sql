DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    ppn money,
    date_from date,
    date_to date,
    constraint fk_spaces foreign key(user_id)
        references users(id)
        on delete cascade
);