from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import time
import json
import threading

app = Flask(__name__)
app.debug = True
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


# GET Request
@app.route("/hello")
@cross_origin()
def hello_world():
    return "Hello World"


# POST Request
@app.route("/data", methods=['POST'])
@cross_origin()
def get_data():
    data = request.get_json(silent=True)
    print("Data from Next Frontend: ", data)

    result = {
        "message": "Successfully Done",
        "status_code": 200
    }
    return app.make_response(jsonify(result))


@app.route("/events", methods=['GET'])
def sse_request():
    """
    Stream events to the client via SSE.
    """
    return Response(data_stream(), mimetype='text/event-stream')


@app.route("/create-course", methods=['GET'])
@cross_origin()
def create_course():
    """
    Simulate a long-running process that sends events to the /events endpoint.
    """
    global event_data

    # Event 1: Getting Video ID
    event_data.append({"data": "Getting Video ID"})
    time.sleep(2)

    # Event 2: Extracting description
    event_data.append({"data": "Extracting description"})
    time.sleep(2)

    # Event 3: Saving to the database
    event_data.append({"data": "Saving to the database"})
    time.sleep(2)

    # Final Event: Process done
    event_data.append({"data": "Course creation completed"})
    time.sleep(2)

    return "Done"


if __name__ == "__main__":
    # Start the Flask app
    app.run(debug=True, port=5000)
