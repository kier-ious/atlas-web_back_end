-- Task1, adding country column
-- SQL script that creates a table users if it doesn't exist

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
  PRIMARY KEY (id),
  UNIQUE (email)
);
