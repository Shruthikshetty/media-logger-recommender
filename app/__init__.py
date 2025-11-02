from flask import Flask
from flask_restful import Api
from config import Config  
from .resources.games import SimilarGames


def create_app(config_class=Config): # Use the base Config by default
    """Application factory pattern"""
    app = Flask(__name__)
    # Load configuration from the Config object
    app.config.from_object(config_class)

    # Initialize extensions with the app
    api = Api(app)

    #Add resources to the api
    api.add_resource(SimilarGames, "/similar/games")

    # define the base route
    @app.route("/")
    def home():
        return "Media logger recommendation api is running."

    return app
