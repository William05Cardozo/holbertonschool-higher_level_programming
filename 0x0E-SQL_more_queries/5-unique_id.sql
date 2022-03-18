-- We create a new table call unique_id
-- with paramethers id and name
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
