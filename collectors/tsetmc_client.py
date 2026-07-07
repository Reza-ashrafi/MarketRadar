import requests


class TSETMCClient:

    def get(self, url):

        print("REQUEST:", url)

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30
        )

        print("STATUS:", response.status_code)

        return response.text
