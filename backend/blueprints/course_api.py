import sys
sys.path.append("../../backend")

from backend.db_connection import conn
from flask import jsonify, request
# sample_blueprint.py
from flask import Blueprint



# just like `app = Flask(__name__)`
COURSE_BLUEPRINT = Blueprint('course', __name__)

@COURSE_BLUEPRINT.route("/fuck", methods=['GET'])
def get_fucked():
    return "<h1>Fuck you too</h1>"

@COURSE_BLUEPRINT.route("/get-courses", methods=['GET'])
def get_all_course_metadata():
    user_id = request.args.get("userID")
    if(user_id is None):
        return []
    cursor = conn.cursor()

    SQL = "SELECT * FROM courses WHERE generated_by=(%s);"
    cursor.execute(SQL, [user_id])

    courses = cursor.fetchall()
    courses_list = []
    for course in courses:
        course_dict = dict()
        fields = ['course_id', 'course_name', 'video_id', 'generated_date', 'completed', 'generated_by']
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

@COURSE_BLUEPRINT.route("/get-course-name")
def return_course_name():
    courseID = request.args.get("courseID")
    print("Here", request.args.get("courseID"))
    cursor = conn.cursor()
    SQL = "SELECT course_name FROM courses WHERE course_id = %s"
    data = [courseID]

    cursor.execute(SQL, data)
    course_name = cursor.fetchone()[0]

    return course_name