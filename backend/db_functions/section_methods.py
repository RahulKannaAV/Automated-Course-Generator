import logging
from backend.db_functions.db_connection import create_connection
from typing import List, Dict

def create_new_section(data_objects: List[Dict]):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Insertion query
        SQL = ("INSERT INTO sections (course_id, section_name, section_start, section_end, section_completed)"
           " VALUES (%s, %s, %s, %s, %s)")

        for idx, data_obj in enumerate(data_objects):
            data = [
                data_obj['course_id'],
                data_obj['section_name'],
                data_obj['section_start'],
                data_obj['section_end'],
                data_obj['section_completed']
                ]

            cursor.execute(SQL, data)
            conn.commit()
            print(f"Inserted {idx+1} sections")

        cursor.close()

    except Exception as e:
        logging.error(f"Failed to create sections: {e}")
    conn.close()
# create_new_section([{"course_id": 8, "section_name": "Fuck you", "section_start": 5, "section_end": 257, "section_completed": False}])

def insert_notes(section_id:int,
                 note_text:str):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        SQL = "UPDATE sections SET notes=(%s) WHERE section_id=(%s)"
        data = [note_text, section_id]

        cursor.execute(SQL, data)
        conn.commit()
        cursor.close()

    except Exception as e:
        logging.error(f"Error in updating notes: {e}")
    conn.close()

def get_section_title_and_course_title(section_id):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        SECTION_NAME_QUERY = "SELECT section_name, course_id FROM sections WHERE section_id=(%s)"

        cursor.execute(SECTION_NAME_QUERY, [section_id])
        data = cursor.fetchone()
        section_name = data[0]

        COURSE_NAME_QUERY = "SELECT course_name FROM courses WHERE course_id=(%s)"

        cursor.execute(COURSE_NAME_QUERY, [data[-1]])
        course_name = cursor.fetchone()[0]

        query_string = f"{course_name} {section_name} "

        conn.close()
        return query_string

    except Exception as e:
        logging.error(f"Error in fetching Course Name and Section Name: {e}")
        return ""

"""
# TEST RUN
section_list = [
    {
        "course_id": 1,
        "section_name": "Course Introduction",
        "section_start": 0,
        "section_end": 276,
        "section_completion": False
    },
    {
        "course_id": 1,
        "section_name": "Introduction of the Instructor",
        "section_start": 277,
        "section_end": 352,
        "section_completion": False
    },
]
"""

