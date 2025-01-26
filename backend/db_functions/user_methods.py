import logging

from backend.db_functions.db_connection import create_connection
from typing import List, Dict


def add_new_user(infoDict: Dict):
    conn = create_connection()

    cursor = conn.cursor()

    try:
        new_user_query = "INSERT INTO users (email_id, name) VALUES (%s, %s) RETURNING user_id"

        data = [infoDict["email"], infoDict["name"]]

        cursor.execute(new_user_query, data)
        logging.info("New user added successfully")
        user_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()

        return str(user_id)

    except Exception as e:
        logging.error(f"Failed to add new user: {e}")
        return None


def check_user(email_id):
    conn = create_connection()

    cursor = conn.cursor()

    try:
        check_user_query = "SELECT * FROM users WHERE email_id=(%s)"

        data = [email_id]
        cursor.execute(check_user_query, data)
        logging.info("Checking presence of user")

        user_detail = cursor.fetchall()
        conn.close()

        if(len(user_detail) == 0):
            return False
        else:
            return True

    except Exception as e:
        logging.error(f"Failed to check user: {e}")
        return "-1"

def get_user_id(email_id):
    conn = create_connection()

    cursor = conn.cursor()

    try:
        user_id_query = "SELECT user_id FROM users WHERE email_id=(%s)"
        data = [email_id]

        cursor.execute(user_id_query, data)
        logging.info("Getting user ID")
        user_id = cursor.fetchone()[0]

        return str(user_id)

    except Exception as e:
        logging.error(f"Failed to get User ID: {e}")
        return None
