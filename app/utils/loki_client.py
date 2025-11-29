import time
import json
import requests


class LokiClient:
    """
    This class is used to push logs to loki
    """

    def __init__(self, url: str, labels: dict):
        self.url = url
        self.labels = labels

    def _push(self, level: str, obj):
        ts = str(int(time.time() * 1e9))  # ns timestamp
        line = json.dumps(
            {
                "level": level,
                **(obj if isinstance(obj, dict) else {"data": obj}),
            },
            default=str,
        )

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

    def info(self, obj):
        self._push("INFO", obj)

    def error(self, obj):
        self._push("ERROR", obj)

    def warning(self, obj):
        self._push("WARNING", obj)

    def debug(self, obj):
        self._push("DEBUG", obj)
