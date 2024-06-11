-- Task 5, Email validation
-- SQL script to create trigger
CREATE TRIGGER reset_valid_email_on_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
      SET NEW.valid_email = 0;
    END IF;
END;