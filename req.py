import mysql.connector as connector
import datetime

# Connect to DB

db = connector.connect(
  host = "localhost",
  username = "root",
  password = "rootroot",
  database = "students_db"
)

cursor = db.cursor()

def register_student(student_name, level_id, mobile_number, email, BOD):
  sql = "INSERT INTO students (student_name, level_id, mobile_number, email, BOD) VALUES (%s, %s, %s, %s, %s)"
  data = (student_name, level_id, mobile_number, email, BOD)
  cursor.execute(sql, data)

  # Save to DB
  db.commit()
  cursor.close()
  db.close()

  print("Student registered successfully with id:", student_id)

def course_enrollment(student_id, course_id):
  # Get the level of the student
  sql = "SELECT level_id FROM students WHERE student_id = %s"
  data = (student_id)
  cursor.execute(sql, data)
  student_level = cursor.fetchone()[0]

  # Get the level of the course
  sql = "SELECT level_id FROM courses WHERE course_id = %s"
  data = (course_id)
  cursor.execute(sql, data)
  course_level = cursor.fetchone()[0]

  # Check if the levels match
  if student_level != course_level:
    print("Error: student and course levels do not match")
    return

  # Check if the student is already enrolled in the course
  sql = "SELECT * FROM enrollment_history WHERE student_id = %s AND course_id = %s"
  cursor.execute(sql, (student_id, course_id))
  result = cursor.fetchone()

  if result:
    print("Error: student is already enrolled in this course")
    return

  # Get the current enrollment count for the course
  sql = "SELECT COUNT(*) FROM enrollment_history WHERE course_id = %s"
  cursor.execute(sql, (course_id))
  enrollment_count = cursor.fetchone()[0]

  # Get the maximum capacity for the course
  sql = "SELECT max_capacity FROM courses WHERE course_id = %s"
  cursor.execute(sql, (course_id,))
  max_capacity = cursor.fetchone()[0]

  # Check if the course is full
  if enrollment_count >= max_capacity:
    print("Error: course is full")
    return

  # Otherwise, enroll the student in the course
  sql = "INSERT INTO enrollment_history (student_id, course_id, enroll_date) VALUES (%s, %s, %s)"
  cursor.execute(sql, (student_id, course_id, datetime.datetime.now()))

  # Save to DB
  db.commit()

  cursor.close()
  db.close()

  print("Student enrolled successfully in course with id:", course_id)

# Create a new course
def create_course(course_id, course_name, max_capacity, hour_rate):
  # Insert a new course into the courses table
  sql = "INSERT INTO courses (course_id, course_name, max_capacity, hour_rate) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, (course_id, course_name, max_capacity, hour_rate))

  # Commit the transaction
  db.commit()
  cursor.close()
  db.close()

  print("Course created successfully with id:", course_id)

# Create a course schedule
def create_course_schedule(day, course_id, start_time, duration):
  # Check if there is already a schedule for the same course at the same time slot
  sql = "SELECT * FROM course_schedule WHERE course_id = %s AND day = %s AND start_time = %s AND duration = %s"
  cursor.execute(sql, (course_id, day, start_time, duration))
  result = cursor.fetchone()

  if result:
    print("Error: a schedule already exists for this course at the same time slot")
    return

  # Insert a new row into the course_schedule table
  sql = "INSERT INTO course_schedule (day, course_id, start_time, duration) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, (day, course_id, start_time, duration))

  db.commit()
  cursor.close()
  db.close()

  print("Course schedule created successfully")

def display_student_schedule(student_id):
  # Get the course schedule for the student
  sql = """
  SELECT c.course_name, cs.day, cs.start_time, cs.duration
  FROM courses c
  INNER JOIN enrollment_history e ON c.course_id = e.course_id
  INNER JOIN course_schedule cs ON c.course_id = cs.course_id
  WHERE e.student_id = %s
  """
  cursor.execute(sql, (student_id))
  result = cursor.fetchall()

  # Print the course schedule
  if result:
    print("Course schedule for student with id {}:".format(student_id))

    # Loop for the available schedules
    for row in result:
      course_name, day, start_time, duration = row
      print("{}, {}, {}, {}".format(course_name, day, start_time, duration))
  else:
    print("No course schedule found for student with id:", student_id)

  cursor.close()
  db.close()