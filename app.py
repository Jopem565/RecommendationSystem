from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

#Load data by accessing the MovieLens Dataset files
ratings = pd.read_csv('ml-latest-small/ratings.csv')
movies = pd.read_csv('ml-latest-small/movies.csv')


# Create User-Item Matrix
user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
user_item_matrix = user_item_matrix.fillna(0)

# Calculate Item-Item Similarity
item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# def predict_ratings(user_id):
#     user_ratings = user_item_matrix.loc[user_id].values
#     sim_scores = item_similarity_df.values
#     weighted_ratings = np.dot(user_ratings, sim_scores)
#     sum_sim_scores = np.abs(sim_scores).sum(axis=1)
#     predicted_ratings = weighted_ratings / sum_sim_scores
#     return predicted_ratings

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_genres = request.form.getlist('genres')
    # time_period = request.form['time_period']
    # if time_period == '2000s_or_higher':
    #     filtered_movies = movies[movies['year'] >= 2000]
    # elif time_period == 'older_than_2000':
    #     filtered_movies = movies[movies['year'] < 2000]
    # else:
    #     filtered_movies = movies

    # Filter movies by selected genres
    recommended_movies = movies[movies['genres'].str.contains('|'.join(selected_genres))]
    return render_template('recommend.html', movies=recommended_movies.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)