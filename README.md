# Movie Recommendation System

This project is a web-based application that provides movie recommendations based on user-selected genres and time periods. It utilizes machine learning techniques to suggest movies from a dataset of movie ratings.

## Features

- **Movie Recommendations:** Get movie suggestions based on selected genres and time periods.
- **Search Functionality:** Search for specific movies within the recommendations.
- **User-Friendly Interface:** Simple and intuitive UI for easy navigation and use.

## Project Structure

- `app.py`: Main Flask application file that handles routes, recommendations, and search functionality.
- `templates/`: Directory containing HTML templates (`index.html` and `recommend.html`).
- `static/`: Directory containing static files such as CSS.
- `ml-latest-small/`: Directory containing the dataset (`movies.csv` and `ratings.csv`).

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/RecommendationSystem.git
    cd RecommendationSystem
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  #On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure the dataset files are in place:**
    Place the `movies.csv` and `ratings.csv` files in the `ml-latest-small/` directory.

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Use the web interface to get movie recommendations:**
    - Select genres and time periods to get recommendations.
    - Use the search bar to find specific movies within the recommendations.

## Machine Learning

The recommendation system uses collaborative filtering techniques to predict user preferences and suggest movies. The key components include:

- **User-Item Matrix:** Constructed from the movie ratings dataset.
- **Similarity Calculation:** Computes similarity between movies or users.
- **Prediction:** Generates movie recommendations based on similar user preferences.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## Acknowledgements

- The movie dataset used in this project is sourced from [MovieLens](https://grouplens.org/datasets/movielens/).
