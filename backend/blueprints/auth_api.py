
from authlib.integrations.flask_client import OAuth
from authlib.oauth2.client import OAuth2Client
from flask import Flask, url_for, make_response, redirect, request, session
from datetime import timedelta
import os
from flask import session, Blueprint
from backend.user_methods import check_user, add_new_user, get_user_id
from functools import wraps
from backend.main import app
def login_required(f):
    @wraps(f) # makes sure that function 'f' retains the correct metadata
    def decorated_function(*args, **kwargs):
        user = dict(session).get('email', None)
        # You would add a check here and usethe user id or something to fetch
        # the other data for that user/check if they exist
        if user: # If user is there, it means user is authenticated
            return f(*args, **kwargs)
        return redirect("/")
    return decorated_function


#Authlib
oauth = OAuth(app)
AUTH_BLUEPRINT = Blueprint('auth', __name__)




#Register google outh

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration' #provide us with common metadata configurations
google = oauth.register(
  name='google',
  server_metadata_url=CONF_URL,
  # Collect client_id and client secret from google auth api
  client_id= os.environ.get("CLIENT_ID"),
  client_secret = os.environ.get("CLIENT_SECRET"),
  client_kwargs={
    'scope': 'openid email profile'
  }
)

@AUTH_BLUEPRINT.route("/start-login", methods=['GET'])
def index():
    print(f"Before Login: {session.items()}")
    return "<a href='/google-login'>Login</a>"

#Routes for login
@AUTH_BLUEPRINT.route('/google-login')
def googleLogin():
    redirect_uri = url_for('auth.authorize', _external=True)
    google = oauth.create_client('google')
    return google.authorize_redirect(redirect_uri)


@AUTH_BLUEPRINT.route('/login/callback')
def authorize():
    token = oauth.google.authorize_access_token()
    user = token['userinfo']
    session['email'] = user['email']
    session['username'] = user['given_name']
    session.permanent = True

    userPresent = check_user(user['email'])

    if(userPresent):
        userID = get_user_id(user['email'])
        session['userID'] = userID

        print(f"After Login: {session.items()}")
        response = make_response(redirect("http://localhost:3000"))
        response.set_cookie("username", user["given_name"])
        response.set_cookie("userID", session['userID'])


    else:
        infoDict = {"email": user["email"], "name": user["given_name"]}
        user_id = add_new_user(infoDict)
        session['userID'] = user_id

        response = make_response(redirect("http://localhost:3000"))
        response.set_cookie("username", user["given_name"])
        response.set_cookie("userID", session['userID'])

    return response


@AUTH_BLUEPRINT.route("/logged")
@login_required
def logged_in(): # same as login_required(logged_in()), if true, returns logged_in, otherwise redirects to home
    return "<div> <h1>You have successfully Logged In</h1> <a href='/logout'>Log Out</a> </div>"

@AUTH_BLUEPRINT.route("/logout")
def logout():
    for key in list(session.keys()):
        session.pop(key)
    cookie = make_response(redirect("http://localhost:3000"))
    cookie.set_cookie("userID", "" ,max_age=0)
    cookie.set_cookie("username", "",max_age=0)
    return cookie


