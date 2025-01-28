import datetime
import pandas as pd
from typing import Tuple, List, Dict
from backend.db_functions.db_connection import conn
from csv import DictWriter
import random

def insert_course_detail(data_obj: Dict):
    curr = conn.cursor()
    SQL = "INSERT INTO courses (course_name, video_id, generated_date, completed, generated_by) VALUES (%s, %s, %s, %s, %s) RETURNING course_id;"

    data = [data_obj["course_name"],
            data_obj["video_id"],
            datetime.datetime.now(),
            "FALSE", int(data_obj["userID"])]

    curr.execute(SQL, data)
    course_id = curr.fetchone()[0]

    conn.commit()
    curr.close()

    csv_data = pd.read_csv("data/Courses.csv")
    taken_courses = set(csv_data['courseName'])

    with open("data/Modified_Course_Data.csv", 'a') as f:
        rating = random.randint(5, 10)
        skill = random.randint(4,10)
        csv_course_id = course_id

        # If the course is already present in the csv file, add the existing courseID to the course transaction
        if data_obj['course_name'] in taken_courses:
            csv_course_id = csv_data[csv_data['CourseName'] == data_obj['course_name']]["courseID"]

        csv_row = {"UserID": f"U{data_obj["userID"]}",
                   "CourseName": data_obj["course_name"],
                   "RatingOfCourse": rating,
                   "UserSkillLevel": skill,
                   "courseID": csv_course_id,
                   "userLabel": data_obj["userID"]}

        dWriter = DictWriter(f, fieldnames=csv_row.keys())
        dWriter.writerow(csv_row)

    print("Course Transactions updated")

    # If the course is already present in the csv file, no need to add it
    if data_obj['course_name'] not in taken_courses:
        with open("data/Courses.csv", 'a') as f:
            course_row = {"courseCode": course_id, "courseName": data_obj["course_name"]}

            courseWriter = DictWriter(f, fieldnames=course_row.keys())
            courseWriter.writerow(course_row)

    print("Course data updated")


    return course_id


