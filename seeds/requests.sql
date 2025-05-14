DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    request_sender INT,
    space_owner INT,
    message_content text,
    space_requested INT,
    dates_requested DATE ARRAY,
    accepted boolean,
    constraint fk_request_sender foreign key(request_sender)
        references users(id)
        on delete cascade,
    constraint fk_space_owner foreign key (space_owner)
        references users (id)
        on delete cascade,
    constraint fk_space_requested foreign key (space_requested)
        references spaces (id)
        on delete cascade
);