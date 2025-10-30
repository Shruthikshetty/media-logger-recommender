# config.py
import os

class Config:
    """
    Base configuration settings.
    The DEBUG flag is controlled by the FLASK_DEBUG environment variable.
    """
    # Reads the FLASK_DEBUG environment variable.
    # Defaults to False if the variable is not set.
    # The check for 'true', '1', 't' makes it flexible.
    DEBUG = os.environ.get('FLASK_DEBUG', '0').lower() in ['true', '1', 't']