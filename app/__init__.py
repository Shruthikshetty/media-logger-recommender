from flask import Flask
from flask_restful import Api
from app.middleware.logging import request_logger
from app.resources.tv_show import SimilarTVShows
from config import Config
from .resources.games import SimilarGames
from .resources.movies import SimilarMovies


def create_app(config_class=Config):  # Use the base Config by default
    """Application factory pattern"""
    app = Flask(__name__)
    # Load configuration from the Config object
    app.config.from_object(config_class)
    # add middleware
    request_logger(app)

    # Initialize extensions with the app
    api = Api(app)

    # Add resources to the api
    api.add_resource(SimilarGames, "/similar/games/<string:id>")
    api.add_resource(SimilarMovies, "/similar/movies/<string:id>")
    api.add_resource(SimilarTVShows, "/similar/tv-shows/<string:id>")

    # define the base route
    @app.route("/")
    def home():
        return "Media logger recommendation api is running."

    return app
