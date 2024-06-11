-- Task 9,  Optimize search and score
-- SCript that creates index in names table and 1st letter of name
CREATE INDEX idx_name_first_score ON names(name(1), score);
