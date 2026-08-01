-- unique_id: id INT unique default 1, name VARCHAR(256), no fail if exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
