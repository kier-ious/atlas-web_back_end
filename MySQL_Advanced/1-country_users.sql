-- Task 1, In and not out
-- Modifies users table with country column

-- Adding country column
ALTER TABLE users
ADD COLUMN country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US' AFTER name;

-- Modifying the email coumn to be UNIQUE
ALTER TABLE users
MODIFY COLUMN email VARCHAR(255) NOT NULL UNIQUE;

-- Add the default country 'US' for existing rows where country isn't set
UPDATE users
SET country = 'US'
WHERE country is NULL;


