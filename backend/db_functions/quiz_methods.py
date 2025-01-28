import logging

from backend.db_functions.db_connection import create_connection
def fetch_questions_from_db(section_id):
    conn = create_connection()
    cursor = conn.cursor()

    all_questions = []

    try:
        QUESTIONS_QUERY = "SELECT quiz_id, quiz_question, correct_option, difficulty FROM quizzes WHERE section_id=(%s)"
        print(section_id)
        cursor.execute(QUESTIONS_QUERY, [section_id])
        question_data = cursor.fetchall()
        for question in question_data:
            question_obj = dict()
            question_obj['question_text'] = question[1]
            question_obj['answer_option'] = question[2]
            question_obj['question_id'] = question[0]
            question_obj['difficulty'] = question[3]

            # Querying Options for the Questions
            OPTIONS_QUERY = "SELECT option_id, option_text FROM choices WHERE quiz_id=(%s)"
            cursor.execute(OPTIONS_QUERY, [question[0]])
            options = cursor.fetchall()
            question_obj['options'] = [option[1] for option in options]

            all_questions.append(question_obj)

        return all_questions

    except Exception as e:
        logging.error(f"Error in fetching quiz questions from database: {e}")
        return []

def insert_quiz_questions_in_db(section_ID, quiz_data):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        QUESTION_INSERT_QUERY = "INSERT INTO quizzes (section_id, quiz_question, correct_option, difficulty) VALUES (%s, %s, %s, %s) RETURNING quiz_id"
        print(quiz_data)
        for idx, question in enumerate(quiz_data):
            cursor.execute(QUESTION_INSERT_QUERY, [section_ID, quiz_data[idx]['question_text'], quiz_data[idx]['answer_option'], quiz_data[idx]['difficulty']])
            conn.commit()

            quiz_id = cursor.fetchone()[0]
            print(f"Questions {quiz_id} added successfully.")
            OPTION_INSERT_QUERY = "INSERT INTO choices (quiz_id, option_id, option_text) VALUES (%s, %s, %s)"
            for idx, option in enumerate(quiz_data[idx]['options']):
                cursor.execute(OPTION_INSERT_QUERY, [quiz_id, idx, option])
                conn.commit()
                print(f"Option {idx} of Quiz ID added successfully.")

    except Exception as e:
        logging.error(f"Error in inserting records to quiz table: {e}")