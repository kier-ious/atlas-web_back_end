-- Task 10, Safe divide
-- Script that creates a function that divides and returns something
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
  IF b = 0 THEN
    SET result = 0;
  ELSE
    SET result = a / b;
  END IF;
  RETURN result;
END //
