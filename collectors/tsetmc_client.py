import requests

from config.settings import REQUEST_TIMEOUT, RETRY_COUNT


class TSETMCClient:

    def __init__(self):
        self.timeout = REQUEST_TIMEOUT


    def get(self, url):

        print("TSETMC REQUEST START")

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            print("STATUS:", response.status_code)

            print("LENGTH:", len(response.text))

            return response.text

        except Exception as e:

            print("REQUEST ERROR:")
            print(e)

            raise e
