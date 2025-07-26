DROP TABLE IF EXISTS badges;

CREATE TABLE badges (
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id     INTEGER NOT NULL,
    name        TEXT    NOT NULL,
    awarded_at  TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO badges (user_id, name) VALUES
  (1, 'Admin'),
  (2, 'Contributor'),
  (3, 'Viewer');