import datetime
import data_retrieval_methods
import desc_extractor
import section_methods
from classes.MessageAnnouncer import MessageAnnouncer
from flask import Flask, request, jsonify, Response, make_response
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import json
import time
import course_methods
from blueprints.section_api import SECTION_BLUEPRINT
from blueprints.course_api import COURSE_BLUEPRINT


load_dotenv()
app = Flask(__name__)
app.register_blueprint(COURSE_BLUEPRINT)
app.register_blueprint(SECTION_BLUEPRINT)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Shared event data
event_data = []


def data_stream():
    """
    A generator that yields data to the client via SSE.
    """
    global event_data
    while True:
        if event_data:
            # Yield the most recent event data and then clear the list
            data = event_data.pop(0)
            yield f'data: {json.dumps(data)}\n\n'
        time.sleep(1)  # Prevent excessive CPU usage if no events are present


@app.route("/events", methods=['GET'])
def sse_request():
    """
    Stream events to the client via SSE.
    """
    return Response(data_stream(), mimetype='text/event-stream')



#######################################

@app.route("/new-course", methods=['POST'])
@cross_origin()
def create_new_course():
    if(request.method == "POST"):
        # Getting Title and URL from the Frontend

        data = request.json

        data_obj = data.copy()

        # To send event info to client
        event_data.append({"data": "Extracting Video ID from Course URL"})

        video_id = data_retrieval_methods.get_video_id(data_obj["course_url"])
        data_obj["video_id"] = video_id

        print(data_obj)
        # Event 2: Extracting description
        event_data.append({"data": "Extracting description"})
        video_desc_text = data_retrieval_methods.get_youtube_description_text(video_id)

        # Event 3: Saving to the database
        event_data.append({"data": "Saving to the database"})
        course_id = course_methods.insert_course_detail(data_obj)

        event_data.append({"data": "Extracting Timestamps"})
        # Extracting Timestamps from Description
        timestamp_dict = data_retrieval_methods.get_section_timestamps(video_desc_text)

        event_data.append({"data": "Creating Course Sections"})
        # Preparing Section lists
        section_list = data_retrieval_methods.prepare_section_list(course_id, timestamp_dict)

        # Using list to create sections
        section_methods.create_new_section(section_list)

        # Final Event: Process done
        event_data.append({"data": "Course creation completed"})

        result = {
            "message": "Course successfully created",
            "status_code": 200
        }
        return app.make_response(jsonify(result))



if(__name__ == "__main__"):
    app.run(debug=True, port=5000)
