# this file contains configuration for loki logger
import time
import os
from app.utils.loki_client import LokiClient

# get config variables
LOKI_URL = os.getenv("LOKI_URL", "")

# create loki logger
loki_logger = LokiClient(
    url=LOKI_URL,
    labels={"app": "media-logger-recommender"},
)
