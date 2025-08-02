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

**Backend**
    - The backend is built using Flask, a lightweight Python web framework. It handles:
    
    - Routing between pages (/, /recommend, etc.)
    
    - Processing user input from forms (genres and year filters)
    
    - Reading and filtering data from the MovieLens dataset (movies.csv and ratings.csv)
    
    - Generating personalized movie recommendations based on genre and time period
    
    - Rendering templates with the recommended movie results

**Frontend**
    - The frontend is built with HTML, CSS, and Jinja2 templates (Flask’s templating engine). It includes:
    
    - A home page (index.html) where users can select their preferred genres and time range
    
    - A results page (recommend.html) that displays the recommended movies dynamically
    
    - Clean and simple styling for ease of use and clarity
    
    - A search bar feature to quickly locate movies within the recommendations


## Database

- The movie dataset used in this project is sourced from [MovieLens](https://grouplens.org/datasets/movielens/).
