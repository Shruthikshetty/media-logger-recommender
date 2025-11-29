# this file contains configuration for loki logger
import time
import os
import logging

import requests

# get config variables
LOKI_URL = os.getenv("LOKI_URL", "")

# create loki logger
logger = logging.getLogger("media-logger-recommender")
logger.setLevel(logging.INFO)

# build simple loki handler
class SimpleLokiHandler(logging.Handler):
    def __init__(self, url, labels):
        super().__init__()
        self.url = url
        self.labels = labels

    def emit(self, record):
        ts = str(int(time.time() * 1e9))  # current time in ns
        line = self.format(record)
        payload = {
            "streams": [
                {
                    "stream": self.labels,
                    "values": [[ts, line]],
                }
            ]
        }
        try:
            requests.post(self.url, json=payload, timeout=5)
        except Exception as e:
            print("Loki error:", e)

logger = logging.getLogger("media-logger-recommender")
logger.setLevel(logging.INFO)

handler = SimpleLokiHandler(
    url=LOKI_URL,
    labels={"app": "media-logger-recommender"},
)
logger.addHandler(handler)
# Export LOGGER - has .info(), .error()!
loki_logger = logger
