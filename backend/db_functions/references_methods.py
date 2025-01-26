import logging

from backend.db_functions.db_connection import create_connection

def get_references_from_db(section_id):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        QUERY = "SELECT * FROM reference WHERE section_id=(%s)"

        print("Fetching Reference records...")
        cursor.execute(QUERY, [section_id])
        records = cursor.fetchall()
        print("References fetched successfully...")

        return records

    except Exception as e:
        logging.error(f"Error in fetching References from Database: {e}")
        return []
