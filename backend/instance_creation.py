from flask import Flask
from flask_cors import CORS
from blueprints.rec_sys_api import RECSYS_BLUEPRINT
from blueprints.section_api import SECTION_BLUEPRINT
from blueprints.auth_api import AUTH_BLUEPRINT
from blueprints.course_api import COURSE_BLUEPRINT
from blueprints.genai_api import GEN_BLUEPRINT
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    app.register_blueprint(COURSE_BLUEPRINT)
    app.register_blueprint(SECTION_BLUEPRINT)
    app.register_blueprint(AUTH_BLUEPRINT)
    app.register_blueprint(GEN_BLUEPRINT)
    app.register_blueprint(RECSYS_BLUEPRINT)
    cors = CORS(app,  resources={r"/*": {"origins": "http://localhost:3000"}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.secret_key = "suckmydick"
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    return app