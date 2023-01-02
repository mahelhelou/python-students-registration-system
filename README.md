# Students Registration System

## Write MySQL database with the following information:

1. The schema name is `students_db`
2. Make sure that I will use this schema for Python
3. Inside the schema `students`, put the following tables:
   - `students`, including:
     - `student_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
     - `student_name` VARCHAR(40)
     - `contact_id` INT foreign key
     - `address_id` INT foreign key
     - `level_id` INT foreign key
     - `BOD` date
   - `contacts`, including:
     - `contact_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
     - `mobile_number` VARCHAR(40)
     - `email` VARCHAR(40)
   - `levels`, including:
     - `level_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
     - `level_name` VARCHAR(40)
   - `course_schedule`, including:
     - `course_schedule_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
     - `course_id` INT foreign key
     - `day` VARCHAR(40)
     - `duration` INT
     - `start_time` time
   - `enrollment_history`, including:
     - `enroll_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
     - `student_id` INT foreign key
     - `course_id` INT foreign key
     - `enroll_date` DATETIME
     - `total_hours` INT
     - `total` (`total_hours` \* `rate_per_hour`) Numerical
   - `courses`, including:
     - `course_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
     - `level_id` INT foreign key
     - `course_name` VARCHAR(40)
     - `max_name` VARCHAR(40)
     - `rate_per_hour` Numerical

## Using the Above DB, Design a Python With the Following Requirements:

1. Register new student: Ask for:

   1. name
   2. birth of date
   3. level
   4. mobile number
   5. email

2. Course enrollment: Ask for:

   1. student id
   2. course id
   3. make sure that course level is from the same student level
   4. make sure the student didn't registered the course before
   5. make sure that the course capacity isn't full

3. Create a new course: Ask for:

   1. course code (Course ID)
   2. course name
   3. max course capacity
   4. hour rate (Price)

4. Create course schedule: Ask for:

   1. select day (Weekdays)
   2. course_id
   3. start time
   4. duration
   5. make sure that there are no any record which has the same course id and the same id at the same slot (start time - end time - day)

5. Display students' courses schedule: Ask for:
   1. Ask For student id
   2. Then display student courses schedule

## For the Same Program using Flask, Jinja2, HTML and CSS

- Design web page to display all stored courses in the system
- Design web page to display all registered students in the system
- Design web page to display all stored courses schedules in the system.

## For the Same Program, Using Flask

Design api request to get `student_details`

- api must be GET
- api must be authenticated by an api key
- api response must be json response
