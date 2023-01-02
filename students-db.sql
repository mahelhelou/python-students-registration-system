CREATE DATABASE students_db;

USE students_db;

CREATE TABLE students (
  student_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  student_name VARCHAR(40),
  contact_id INT,
  level_id INT,
  BOD DATE,
  FOREIGN KEY (`contact_id`) REFERENCES contacts(`contact_id`),
  FOREIGN KEY (`level_id`) REFERENCES levels(`level_id`)
);

CREATE TABLE contacts (
  contact_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  mobile_number VARCHAR(40),
  email VARCHAR(40)
);

CREATE TABLE levels (
  level_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  level_name VARCHAR(40)
);

CREATE TABLE course_schedule (
  course_schedule_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  course_id INT,
  day VARCHAR(40),
  duration INT,
  start_time TIME,
  FOREIGN KEY (`course_id`) REFERENCES courses(`course_id`)
);

CREATE TABLE enrollment_history (
  enroll_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  student_id INT,
  course_id INT,
  enroll_date DATETIME,
  total_hours INT,
  total NUMERIC(8,2),
  FOREIGN KEY (`student_id`) REFERENCES students(`student_id`),
  FOREIGN KEY (`course_id`) REFERENCES courses(`course_id`)
);

CREATE TABLE courses (
  course_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  level_id INT,
  course_name VARCHAR(40),
  max_name VARCHAR(40),
  rate_per_hour NUMERIC(8,2),
  FOREIGN KEY (level_id) REFERENCES levels(level_id)
);