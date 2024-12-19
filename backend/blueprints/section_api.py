import sys
sys.path.append("../../backend")
from flask import request, send_file
from io import BytesIO
from gtts import gTTS
from backend.db_connection import conn
from backend.subtitles import extract_section_transcript
from backend.data_retrieval_methods import get_subtitles
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

@SECTION_BLUEPRINT.route("/get-transcript-sequences", methods=['GET'])
def get_sequence_for_typing():
    course_id = request.args.get("course_id")
    start_seconds = request.args.get("from_seconds")
    end_seconds = request.args.get("to_seconds")
    video_id = request.args.get("video_id")

    # Get subtitle sequence for the section
    subtitle_sequence = get_subtitles(video_id=video_id,
                                      from_seconds=int(start_seconds),
                                      to_seconds=int(end_seconds))

    print(subtitle_sequence)

    return subtitle_sequence

@SECTION_BLUEPRINT.route("/play-translation", methods=['GET'])
def get_translated_audio():
    start_seconds = request.args.get("from_seconds")
    end_seconds = request.args.get("to_seconds")
    video_id = request.args.get("video_id")

    # Get subtitle sequence for the section
    section_transcript = extract_section_transcript(video_id=video_id,
                                      from_seconds=int(start_seconds),
                                      to_seconds=int(end_seconds))
    mp3_fp = BytesIO()
    tts = gTTS(section_transcript[:300], lang='en')
    print(section_transcript[:300])
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)  # Reset the pointer to the beginning

    # Send the BytesIO object as a file-like response
    return send_file(mp3_fp, mimetype='audio/mpeg')
