DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    request_sender int,
    space_owner text,
    message_content text,
    space_requested text,
    dates_requested date,
    constraint fk_request_sender foreign key(request_sender)
        references users(id)
        on delete cascade
);