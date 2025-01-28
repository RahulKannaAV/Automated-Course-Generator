from torch.utils.data import Dataset
import torch

class CourseDataset(Dataset):
  def __init__(self, user, course ,rating, user_skill):
    self.userIDs = user
    self.courseIDs = course
    self.courseRatings = rating
    self.userSkills = user_skill


  def __len__(self):
    return len(self.userIDs)

  def __getitem__(self, item):
    userID = self.userIDs[item]
    courseID = self.courseIDs[item]
    courseRating = self.courseRatings[item]
    userSkill = self.userSkills[item]

    return ({
        "userID": userID,
        "courseID": courseID,
        "courseRating": courseRating,
        "userSkill": userSkill
    })
