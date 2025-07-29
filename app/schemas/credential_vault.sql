drop table if exists credentialvault;

create table credentials (
    id serial primary key,
    badge_id text not null,
    is_bot boolean not null default false,
    api_key text not null,
    token text not null,
    service_name text not null,
    account_name text not null,

    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone default now(),
    deleted_at timestamp with time zone
);