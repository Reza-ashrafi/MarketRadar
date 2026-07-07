import requests

from config.settings import REQUEST_TIMEOUT, RETRY_COUNT


class TSETMCClient:

    def __init__(self):
        self.timeout = REQUEST_TIMEOUT

    def get(self, url):
        last_error = None

        for _ in range(RETRY_COUNT):
            try:
                response = requests.get(
                    url,
                    timeout=self.timeout
                )

                if response.status_code == 200:
                    return response.text

            except Exception as e:
                last_error = e

        raise Exception(
            f"TSETMC connection failed: {last_error}"
        )
