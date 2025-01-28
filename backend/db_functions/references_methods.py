import logging

from backend.db_functions.db_connection import create_connection

def get_references_from_db(section_id):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        QUERY = "SELECT reference_heading, reference_url FROM reference WHERE section_id=(%s)"

        print("Fetching Reference records...")
        cursor.execute(QUERY, [section_id])
        records = cursor.fetchall()
        print("References fetched successfully...")

        records = [{"title": record[0], "URL": record[1]} for record in records]

        return records

    except Exception as e:
        logging.error(f"Error in fetching References from Database: {e}")
        return []

def insert_multiple_references(section_id, data_list):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        for idx, data in enumerate(data_list):
            url = data['URL']
            title = data['title']

            QUERY = "INSERT INTO reference (section_id, reference_heading, reference_url) VALUES (%s, %s, %s)"

            cursor.execute(QUERY, [section_id, title, url])
            conn.commit()
            print(f"Inserted Reference {idx+1} of Section ID {section_id}")
        conn.close()

    except Exception as e:
        logging.error(f"Error in inserting references into the database: {e}")
