-- Task 8, Optimize simple search
-- SCript that creates index in names table and 1st letter of name
CREATE INDEX idx_name_first ON names(name(1));
