-- Task 10, Safe divide
-- Script that creates a function that divides and returns something
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
  IF b = 0 THEN
    return = 0;
  ELSE
    return = a / b;
  END IF;
END;
DELIMITER ;
