DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text
);



-- Inserting into the TABLE

INSERT INTO users (username, email, password) VALUES 
('john_doe', 'johndoe@gmail.com', '$2b$12$deQUgswzeqw2yy57MFubguANl/NZodZtcpFTxd/kL67.SePhpcXHu'),
('jane_doe', 'janedoe@gmail.com', '$2b$12$fIvFzbOn9FzromZDrZ5tMO/KkoM5EPsMmC91enUcCtDCCK/57y3A2');

