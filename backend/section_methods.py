import logging

from db_connection import conn
from typing import List, Dict

def create_new_section(data_objects: List[Dict]):
    cursor = conn.cursor()

    try:
        # Insertion query
        SQL = ("INSERT INTO sections (course_id, section_name, section_start, section_end, section_completion)"
           " VALUES (%s, %s, %s, %s, %s)")

        for idx, data_obj in enumerate(data_objects):
            data = [
                data_obj['course_id'],
                data_obj['section_name'],
                data_obj['section_start'],
                data_obj['section_end'],
                data_obj['section_completion']
                ]

            cursor.execute(SQL, data)
            conn.commit()
            print(f"Inserted {idx+1} sections")

        cursor.close()

    except Exception as e:
        logging.error(f"Failed to create sections: {e}")
    conn.close()

def insert_notes(section_id:int,
                 note_text:str):
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