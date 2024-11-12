from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.debug = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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