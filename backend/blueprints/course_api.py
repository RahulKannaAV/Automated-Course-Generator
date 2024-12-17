import sys
sys.path.append("../../backend")

from backend.db_connection import conn
from flask import jsonify, request
# sample_blueprint.py
from flask import Blueprint



# just like `app = Flask(__name__)`
COURSE_BLUEPRINT = Blueprint('course', __name__)

@COURSE_BLUEPRINT.route("/get-courses", methods=['GET'])
def get_all_course_metadata():
    cursor = conn.cursor()

    SQL = "SELECT * FROM courses;"
    cursor.execute(SQL)

    courses = cursor.fetchall()

    courses_list = []
    for course in courses:
        course_dict = dict()
        fields = ['course_id', 'course_name', 'video_id', 'generated_date', 'completed']
        for i in range(len(course)):
            course_dict[fields[i]] = course[i]
        courses_list.append(course_dict)

    cursor.close()
    return courses_list

@COURSE_BLUEPRINT.route("/get-video-id")
def return_video_id():
    courseID = request.args.get("courseID")
    print("Here", request.args.get("courseID"))
    cursor = conn.cursor()
    SQL = "SELECT video_id FROM courses WHERE course_id = %s"
    data = [courseID]

    cursor.execute(SQL, data)
    videoID = cursor.fetchone()[0]

    return videoID