from backend.db_functions.db_connection import create_connection
import logging

def extract_summary_from_db(section_id):

    conn = create_connection()
    cursor = conn.cursor()

    try:
        QUERY = "SELECT * FROM summary WHERE section_id=(%s)"

        cursor.execute(QUERY, [section_id])

        summary_data = cursor.fetchone()
        conn.close()

        return [] if summary_data is None else summary_data

    except Exception as e:
        logging.error(f"Failed to extract summary from database: {e}")
        return []

def add_new_summary(summary_data):
    conn = create_connection()
    cursor = conn.cursor()
    print(f"Summary Data: {summary_data}")

    try:
        QUERY = "INSERT INTO summary (section_id, summary_text) VALUES (%s, %s) RETURNING summary_text"

        cursor.execute(QUERY, summary_data)
        notes_text = cursor.fetchone()
        conn.commit()
        print("New summary added successfully")
        conn.close()
        return notes_text[0]

    except Exception as e:
        logging.error(f"Failed to update summary into the database: {e}")
        return ""

