from torch import nn
import torch

class CourseRecommender(nn.Module):
  def __init__(self, n_users, n_courses,
               embed_size=256,
               hidden_dim=256,
               drop_rate=0.2):
    super().__init__()
    self.num_users = n_users
    self.num_courses = n_courses
    self.embed_size = embed_size
    self.hidden_dim = hidden_dim

    self.user_embedding = nn.Embedding(
        num_embeddings=self.num_users,
        embedding_dim=self.embed_size
    )

    self.course_embedding = nn.Embedding(
        num_embeddings=self.num_courses,
        embedding_dim=self.embed_size
    )

    self.fc1 = nn.Linear(in_features = 2*self.embed_size,
                         out_features = self.hidden_dim)
    self.fc2 = nn.Linear(in_features = self.hidden_dim,
                         out_features = 1)

    # Dropout
    self.dropout = nn.Dropout(p=drop_rate)

    # Activation function
    self.relu = nn.ReLU()

  def forward(self, users, courses):
    # Create embeddings
    embeddings_for_users = self.user_embedding(users)
    embeddings_for_courses = self.course_embedding(courses)

    merged_embeddings = torch.cat([embeddings_for_users, embeddings_for_courses], dim=1)

    # Pass the embeddings to the fully connected
    fc_x = self.fc1(merged_embeddings)
    relu_x = self.relu(fc_x)

    # Dropout to avoid overfitting
    drop_x = self.dropout(relu_x)

    # Final output is calculated by passing it to 2nd fully connected layer
    output = self.fc2(drop_x)

    return output
