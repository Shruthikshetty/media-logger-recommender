# Media Logger Recommendation API

![Python Version](https://img.shields.io/badge/python->=3.8-blue)
![Flask Version](https://img.shields.io/badge/flask-3.1.2-green)
![scikit-learn Version](https://img.shields.io/badge/scikit--learn-1.7.2-orange)

This project provides a RESTful API to generate content-based recommendations for various media types, including games, movies, and TV shows. It uses pre-trained machine learning models to find and return similar items based on a given item ID.

## Features

-   **Content-Based Recommendations**: Generates a list of similar items based on content features.
-   **Multiple Media Types**: Supports recommendations for games, movies, and TV shows through dedicated endpoints.
-   **Scalable Architecture**: Built with a modular Flask application factory pattern, making it easy to extend and maintain.
-   **Lightweight**: No database integration required; models and data are loaded into memory from `.pkl` files.

## Project Structure

The project follows a modular structure to separate concerns, making it clean and scalable.
```txt
/recommendation-api/
|
|-- app/
|   |-- __init__.py             # Application factory to create and configure the Flask app
|   |
|   |-- ml/
|   |   |-- game_model.pkl      # Pre-trained model for game recommendations
|   |   |-- movie_model.pkl     # Pre-trained model for movie recommendations
|   |   |-- tv_show_model.pkl   # Pre-trained model for TV show recommendations
|   |   |
|   |   `-- services/
|   |       |-- __init__.py
|   |       |-- game_service.py # Logic to load and use the game model
|   |       |-- movie_service.py # Logic for the movie model
|   |       `-- tv_show_service.py # Logic for the TV show model
|   |
|   `-- resources/
|       |-- __init__.py
|       |-- games.py            # Defines the /games/... API endpoints
|       |-- movies.py           # Defines the /movies/... API endpoints
|       `-- tv_shows.py         # Defines the /tvshows/... API endpoints
|
|-- config.py                   # Application configuration settings
|-- requirements.txt            # Project dependencies
|-- run.py                      # Main entry point to start the server
`-- README.md                   # This file
```

### Deployment
  This app is deployed on Hugging Face at <https://huggingface.co/spaces/shruthik77/media-logger-recommender-api>

## Getting Started

### Prerequisites

-   Python 3.8+
-   `pip` for package management

### Installation

1.  **Clone the repository:**
    ```
    git clone https://github.com/Shruthikshetty/media-logger-recommender.git
    cd media-logger-recommender
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```
    # On Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```
    pip install -r requirements.txt
    ```

### Running the Application

To run the application in **development mode** (with auto-reloader and debugger), set the `FLASK_DEBUG` environment variable to `1`. 
```bash
set FLASK_DEBUG=1
flask run
```

The API will be available at `http://127.0.0.1:5000`.

