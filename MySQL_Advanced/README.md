# MySQL Advanced Project

## Project Overview
This project focuses on advanced MySQL concepts, aiming to deepen your understanding and skills in database management and optimization. The key areas include creating tables with constraints, optimizing queries with indexes, and implementing stored procedures, functions, views, and triggers in MySQL.

## Learning Objectives

### 1. Creating Tables with Constraints
Creating tables with constraints ensures data integrity and consistency. Constraints are rules applied to table columns to enforce certain conditions.

- **PRIMARY KEY**: Uniquely identifies each row in a table.
- **FOREIGN KEY**: Ensures referential integrity by linking two tables.
- **UNIQUE**: Ensures all values in a column are distinct.
- **NOT NULL**: Ensures a column cannot have a NULL value.
- **CHECK**: Ensures all values in a column satisfy a specific condition.
- **DEFAULT**: Sets a default value for a column if no value is provided.

```sql
-- Create a table with constraints
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    CHECK (email LIKE '%_@__%.__%')
);
