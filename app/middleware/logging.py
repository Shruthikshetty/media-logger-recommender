from venv import logger
from flask import request, g
from app.utils.loki_logger import loki_logger


def request_logger(app):
    """Global request logging middleware"""

    @app.before_request
    def log_request():
        """
        Logs the request before each request is processed.
        """
        raw = request.headers.get("X-Request-Id")
        request_id = raw.split(",")[0].strip() if raw else None

        loki_logger.info(
            {
                "message": f"Incoming request: {request.method} {request.url}",
                "method": request.method,
                "url": request.url,
                "ip": request.remote_addr,
                "requestId": request_id,
                "body": request.get_json(silent=True) or request.data.decode("utf-8"),
            }
        )

    @app.after_request
    def log_response(response):
        """
        Logs the response after each request is processed.
        """
        raw = request.headers.get("X-Request-Id")
        request_id = raw.split(",")[0].strip() if raw else None

        logMessage = {
            "message": f"Outgoing response for: {request.method} {request.url}",
            "method": request.method,
            "statusCode": response.status_code,
            "requestId": request_id,
            "body": response.get_data(as_text=True),
        }
        if response.status_code >= 400:
            loki_logger.error(logMessage)
        else:
            loki_logger.info(logMessage)
        return response
