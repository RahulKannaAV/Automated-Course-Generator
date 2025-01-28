import pandas as pd
from typing import Dict


def get_course_encoder()->Dict:
  course_records = pd.read_csv("data/Courses.csv")
  course_encoder = {course_records["courseCode"][course]: course_records["courseName"][course] for course in range(len(course_records))}

  return course_encoder

def get_user_encoder()->Dict:
  user_records = pd.read_csv("data/Users.csv")
  user_encoder = {user_records["userID"][i]: user_records["userCode"][i] for i in range(len(user_records))}
  return user_encoder
get_user_encoder()
