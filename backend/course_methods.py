import datetime
from typing import Tuple, List, Dict
from db_connection import conn

def insert_course_detail(data_obj: Dict):
    curr = conn.cursor()
    SQL = "INSERT INTO courses (course_name, video_id, generated_date, completed) VALUES (%s, %s, %s, %s) RETURNING course_id;"

    data = [data_obj["course_name"],
            data_obj["video_id"],
            datetime.datetime.now(),
            "FALSE", ]


    curr.execute(SQL, data)
    course_id = curr.fetchone()[0]

    conn.commit()
    curr.close()
    return course_id


