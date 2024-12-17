import sys
sys.path.append("../../backend")
from flask import request
from backend.db_connection import conn
from flask import Blueprint
# just like `app = Flask(__name__)`

SECTION_BLUEPRINT = Blueprint('section', __name__)

@SECTION_BLUEPRINT.route("/sections/<course_id>", methods=['GET'])
def get_all_sections(course_id):
    cursor = conn.cursor()

    # Getting all sections that are from the course
    SQL = "SELECT section_id, section_name FROM sections WHERE course_id=(%s)"
    query = (course_id, )

    cursor.execute(SQL, query)
    sections = cursor.fetchall()

    return sections

@SECTION_BLUEPRINT.route("/get-section-content", methods=['GET'])
def get_section_content():
    sectionID = request.args.get("sectionID")
    print("Sect ", sectionID)

    cursor = conn.cursor()

    SQL = "SELECT section_name, section_start, section_end FROM sections WHERE section_id = %s"
    data = (sectionID, )

    cursor.execute(SQL, data)

    section_row = cursor.fetchall()[0]
    fields = ["section_name", 'section_start', 'section_end']
    section_dict = dict()

    for idx, field in enumerate(fields):
        section_dict[field] = section_row[idx]

    return section_dict
