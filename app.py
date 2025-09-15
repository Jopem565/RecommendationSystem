from flask import Flask, render_template, request
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load data
movies = pd.read_csv('ml-latest-small/movies.csv')
ratings = pd.read_csv('ml-latest-small/ratings.csv')

# Merge movies and ratings dataframes
movie_ratings = pd.merge(movies, ratings, on='movieId')

# User-Item Matrix
user_movie_matrix = ratings_df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_genres = request.form.getlist('genres')
    time_period = request.form.get('time_period')
    min_rating = request.form.get('min_rating')
    min_rating = float(min_rating) if min_rating else 0  
    # Default minimum rating to 0 if not provided
    top_recs = request.form.get('top_recs')
    top_recs = int(top_recs) if top_recs else 0
    #Default top recommendations to 0 if not provided

    # Initially assign recommended_movies to an empty list
    recommended_movies = []

    # Filter based on genres
    if selected_genres:
        genre_filter = movie_ratings['genres'].str.contains('|'.join(selected_genres))
    else:
        genre_filter = pd.Series([True] * len(movie_ratings))

    # Filter based on time period
    if time_period == '2000s_or_higher':
        year_filter = movie_ratings['title'].str.extract(r'\((\d{4})\)')[0].astype(float) >= 2000
    elif time_period == 'older_than_2000':
        year_filter = movie_ratings['title'].str.extract(r'\((\d{4})\)')[0].astype(float) < 2000
    else:
        year_filter = pd.Series([True] * len(movie_ratings))

    # Filter based on rating
    rating_filter = movie_ratings['rating'] >= min_rating

    # Combine filters
    combined_filter = genre_filter & year_filter & rating_filter
    filtered_movies = movie_ratings[combined_filter]


    movie_similarity = cosine_similarity(user_movie_matrix.T)
    movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

    # Get the top recommended movies
    if (top_recs == 0):
        recommended_movies = filtered_movies.drop_duplicates(subset=['movieId']).to_dict(orient='records')
    else:
        recommended_movies = filtered_movies.drop_duplicates(subset=['movieId']).head(top_recs).to_dict(orient='records')

    return render_template('recommend.html', movies=recommended_movies)

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search_query', '')
    search_results = []

    if search_query:
        # Filter movies based on search query
        search_results = movies[movies['title'].str.contains(search_query, case=False)].to_dict(orient='records')

    return render_template('recommend.html', search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True)
