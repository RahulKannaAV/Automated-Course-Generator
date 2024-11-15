from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import time
import json
import threading

app = Flask(__name__)
app.debug = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

