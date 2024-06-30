import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split


# Load the datasets
ratings = pd.read_csv('ml-latest-small/ratings.csv')
movies = pd.read_csv('ml-latest-small/movies.csv')

# Display the first few rows of each DataFrame
print(ratings.head())
print(movies.head())

# Create User-Item Matrix
user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
user_item_matrix = user_item_matrix.fillna(0)

# Split data into training and testing sets
train_data, test_data = train_test_split(user_item_matrix, test_size=0.2, random_state=42)

# Calculate Item-Item Similarity
item_similarity = cosine_similarity(train_data.T)
item_similarity_df = pd.DataFrame(item_similarity, index=train_data.columns, columns=train_data.columns)

# Predict Ratings
def predict_ratings(user_id):
    user_ratings = train_data.loc[user_id].values
    sim_scores = item_similarity_df.values
    weighted_ratings = np.dot(user_ratings, sim_scores)
    sum_sim_scores = np.abs(sim_scores).sum(axis=1)
    predicted_ratings = weighted_ratings / sum_sim_scores
    return predicted_ratings

# Example: Predict ratings for a specific user
user_id = 1
predicted_ratings = predict_ratings(user_id)

# Convert predictions to a DataFrame
predicted_ratings_df = pd.DataFrame(predicted_ratings, index=train_data.columns, columns=['PredictedRating'])
recommended_movies = predicted_ratings_df.sort_values(by='PredictedRating', ascending=False).head(10)

# Display recommended movies
recommended_movie_titles = movies[movies['movieId'].isin(recommended_movies.index)]
print(recommended_movie_titles[['title']])

# Evaluate the model using Mean Squared Error
def mse(predicted, actual):
    mask = actual != 0
    return ((predicted[mask] - actual[mask]) ** 2).mean()

test_users = test_data.index
total_mse = 0
for user in test_users:
    actual_ratings = test_data.loc[user].values
    predicted_ratings = predict_ratings(user)
    total_mse += mse(predicted_ratings, actual_ratings)

average_mse = total_mse / len(test_users)
print(f'Mean Squared Error: {average_mse}')