from flask import Flask
from flask_restful import Api
from config import Config  

def create_app(config_class=Config): # Use the base Config by default
    """Application factory pattern"""
    app = Flask(__name__)
    # Load configuration from the Config object
    app.config.from_object(config_class)

    # define the base route
    @app.route("/")
    def home():
        return "Media logger recommendation api is running."

    return app
