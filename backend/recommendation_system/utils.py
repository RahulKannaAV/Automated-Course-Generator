import torch
from backend.classes.CourseRecommender import CourseRecommender
from backend.recommendation_system.encoder import get_user_encoder, get_course_encoder
from pathlib import Path


def save_model(model_path, model_name, model):

  model_path.mkdir(exist_ok=True, parents=True)

  torch.save(f=model_path/model_name,
           obj=model.state_dict())
  print("Model saved successfully")


def load_model(weights_path, device="cpu"):
  encoder_user = get_user_encoder()
  encoder_course = get_course_encoder()

  loaded_instance = CourseRecommender(n_users=50000,
                                      n_courses=699,
                                      embed_size=128,
                                      hidden_dim=256,
                                      drop_rate=0.5).to(device)

  if(Path(weights_path).is_file()):
  
    loaded_instance.load_state_dict(state_dict=torch.load(f=weights_path,
                                                        weights_only=True,

                                                        map_location=device), strict=False)
    print("Weights Loaded")
  else:
    print("Upload model weights before loading")
  
  return loaded_instance
