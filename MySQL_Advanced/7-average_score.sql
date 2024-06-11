-- Task 7, Average score
-- Script that creates a stores scored average
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

CREATE PROCEDURE ComputeAverageScoreForUser(
  IN user_id INT
)
BEGIN
  DECLARE avg_score FLOAT;
  -- Calculate the average score for the given user_id
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE corrections.user_id = user_id;
  -- Update the average_score in the users table
  UPDATE users
  SET average_score = avg_score
  WHERE id = user_id;
END;

DELIMITER;
