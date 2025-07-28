DROP TABLE IF EXISTS badges;

CREATE TABLE badges (
    badge_id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    badge_name     INTEGER NOT NULL,
    badge_type        TEXT    NOT NULL,
    is_valid BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    validity_period INTERVAL DEFAULT '1 year',
    is_ephemeral BOOLEAN NOT NULL DEFAULT FALSE,
);
