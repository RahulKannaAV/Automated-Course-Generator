from flask import Blueprint, request, current_app as app
from backend.recommendation_system.utils import load_model
from backend.recommendation_system.encoder import get_course_encoder
from backend.recommendation_system.recommender_functions import recommend_courses
import pandas as pd
import torch

RECSYS_BLUEPRINT = Blueprint('rec_sys', __name__)

@RECSYS_BLUEPRINT.route("/get-recommendations")
def get_recommendations():
    userID = int(request.args.get("userID"))
    data = pd.read_csv(app.open_resource("data/Modified_Course_Data.csv"))

    all_courses = data['courseID'].unique()
    done_courses = set(data[data['userLabel'] == userID]['courseID'])

    device = "cuda" if torch.cuda.is_available() else "cpu"

    loaded_model = load_model("recommendation_system/model_weights/Course_Recommender_Model_10_Epochs_v2_good.pth")

    recommendations = recommend_courses(model=loaded_model,
                                        courses=all_courses,
                                        user_id=userID,
                                        top_k=12,
                                        device=device,
                                        done_courses=done_courses)

    course_encoder = get_course_encoder()
    course_recommendations = [course_encoder[courseID] for courseID in recommendations]

    return course_recommendations
