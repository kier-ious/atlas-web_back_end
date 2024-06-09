-- 0-uniq_users.sql
-- SQL script that creates a table users if it doesn't exist

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  PRIMARY KEY (id),
  UNIQUE (email)
);
