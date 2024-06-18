-- Create database
CREATE DATABASE university;

USE university;

-- Students - sid, sname, age, dept
CREATE TABLE students
(
    sid INT(3) PRIMARY KEY,
    sname VARCHAR(30) NOT NULL,
    age INT(3),
    dept VARCHAR(30) CHECK(dept IN ('CSE','ECE','MECH'))
);

-- Courses - cid, cname, credits
CREATE TABLE courses
(
    cid INT(3) PRIMARY KEY,
    cname VARCHAR(50) NOT NULL,
    credits INT(2) NOT NULL
);

-- Enrollments - sid, cid, grade
CREATE TABLE enrollments
(
    sid INT(3),
    cid INT(3),
    grade VARCHAR(2) CHECK(grade IN ('A','B','C','D','F')),
    PRIMARY KEY (sid, cid),
    FOREIGN KEY (sid) REFERENCES students(sid),
    FOREIGN KEY (cid) REFERENCES courses(cid)
);

-- Insert values into the students table
INSERT INTO students (sid, sname, age, dept) VALUES 
(101, 'John Doe', 20, 'CSE'),
(102, 'Jane Smith', 21, 'ECE'),
(103, 'Michael Johnson', 22, 'MECH'),
(104, 'Emily Davis', 20, 'CSE'),
(105, 'Daniel Brown', 21, 'ECE');

-- Insert values into the courses table
INSERT INTO courses (cid, cname, credits) VALUES 
(201, 'Data Structures', 3),
(202, 'Algorithms', 3),
(203, 'Computer Networks', 4),
(204, 'Database Systems', 3),
(205, 'Operating Systems', 4);

-- Insert values into the enrollments table
INSERT INTO enrollments (sid, cid, grade) VALUES 
(101, 201, 'A'),
(101, 202, 'B'),
(102, 203, 'A'),
(103, 204, 'C'),
(104, 205, 'B'),
(105, 201, 'A');

-- Select all students
SELECT * FROM students;

-- Select all courses
SELECT * FROM courses;

-- Select all enrollments
SELECT * FROM enrollments;

-- Update the grade of a student in a course
UPDATE enrollments SET grade = 'A' WHERE sid = 102 AND cid = 203;
SELECT * FROM enrollments;

-- Delete an enrollment
DELETE FROM enrollments WHERE sid = 103 AND cid = 204;
SELECT * FROM enrollments;

-- Add a new column 'email' to the students table
ALTER TABLE students
ADD COLUMN email VARCHAR(50);
SELECT * FROM students;

-- Modify the datatype of the 'credits' column in courses table
ALTER TABLE courses
MODIFY COLUMN credits DECIMAL(3, 1);
SELECT * FROM courses;

-- Rename the 'grade' column in enrollments table to 'final_grade'
ALTER TABLE enrollments
CHANGE COLUMN grade final_grade VARCHAR(2);
SELECT * FROM enrollments;

-- Truncate the enrollments table
TRUNCATE TABLE enrollments;

-- Drop the tables in reverse order of creation to avoid foreign key constraints issues
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;

-- Drop the database university
DROP DATABASE IF EXISTS university;

-- Arithmetic Operators Examples:

-- Addition
SELECT 10 + 5;

-- Subtraction
SELECT 20 - 8;

-- Multiplication
SELECT 5 * 4;

-- Division
SELECT 20 / 4;

-- Modulo
SELECT 15 % 4;

-- Logical Operators Examples:

-- AND
SELECT * FROM students WHERE age > 20 AND dept = 'CSE';

-- OR
SELECT * FROM students WHERE age > 20 OR dept = 'ECE';

-- NOT
SELECT * FROM students WHERE NOT age > 20;

-- IN
SELECT * FROM students WHERE dept IN ('CSE', 'ECE');

-- BETWEEN
SELECT * FROM students WHERE age BETWEEN 20 AND 22;

-- LIKE
SELECT * FROM students WHERE sname LIKE 'J%';

-- IS NULL
SELECT * FROM students WHERE email IS NULL;