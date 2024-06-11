-- Task 10, Safe divide
-- Script that creates a function that divides and returns something
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 10)
DETERMINISTIC
BEGIN
  DECLARE result DECIMAL(10, 10);
  IF b = 0 THEN
    SET result = 0;
  ELSE
    SET result = a / b;
  END IF;
  RETURN result;
END //
