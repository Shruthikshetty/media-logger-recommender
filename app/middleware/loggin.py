from venv import logger
from flask import request, g
from app.utils.loki_logger import loki_logger

def request_logger(app):
    """Global request logging middleware"""
    print("registering request_logger")  # should appear once on startup

    @app.before_request
    def log_request():
        """
        Logs the request before each request is processed.
        """
        loki_logger.info(f"Request: {request}")

    @app.after_request
    def log_response(response):
        """
        Logs the response after each request is processed.
        """
        body = response.get_data(as_text=True)
        loki_logger.info(f"Response: {response}")
        return response
