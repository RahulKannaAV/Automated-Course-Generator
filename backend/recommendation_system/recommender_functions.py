import pandas as pd
import torch
from backend.recommendation_system.encoder import get_user_encoder, get_course_encoder
from backend.recommendation_system.utils import load_model

def recommend_courses(model, user_id, courses, done_courses, device, top_k=10, batch_size=50):
  model.eval()
  not_touched_courses = [i for i in courses if i not in done_courses]
  preds = []

  with torch.no_grad():
    for unseen in range(0, len(not_touched_courses), batch_size): # Going through all batches of courses
      unseen_courses_batch = not_touched_courses[unseen: unseen+batch_size] # Creating a batch of unseen courses
      user_id_tensor = torch.tensor([user_id] * len(unseen_courses_batch)).to(device) # Creating user_id tensor of same dimension
      courses_tensor = torch.tensor(unseen_courses_batch).to(device)

      pred_ratings = model(user_id_tensor, courses_tensor).view(-1).tolist() # view(-1) reduces the dimensions of the individual tensor value
      preds.extend(zip(unseen_courses_batch, pred_ratings))

    preds.sort(key=lambda x: x[1], reverse=True) # Descending order sort based on ratings (highest rating courses comes first)
    top_courses = [course_id for course_id, _ in preds[:top_k]] # Taking upto k courses through list comprehension

    return top_courses


def get_course_names(recommendations):
  course_encoder = get_course_encoder()
  course_names = [course_encoder[courseID] for courseID in recommendations]

  return course_names

