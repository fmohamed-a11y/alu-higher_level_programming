-- id_not_null: id INT default 1, name VARCHAR(256), no fail if exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
