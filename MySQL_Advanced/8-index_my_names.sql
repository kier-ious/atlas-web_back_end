-- Task 8, Optimize simple search
-- SCript that creates index in names table and 1st letter of name
SELECT INDEX idx_name_first ON names (LEFT(name, 1));
