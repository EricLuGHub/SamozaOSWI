drop table if exists credentials;

create table credentials (
    id serial primary key,
    is_bot boolean not null default false,
    service_name text not null,
    user_id integer,
    connection_id integer not null,

    access_token text,
    refresh_token text,

    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone default now(),
    deleted_at timestamp with time zone
);