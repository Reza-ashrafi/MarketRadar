import requests

from config.settings import REQUEST_TIMEOUT, RETRY_COUNT


class TSETMCClient:

    def __init__(self):
        self.timeout = REQUEST_TIMEOUT


    def get(self, url):

        print("TSETMC REQUEST START")

        last_error = None

        for i in range(RETRY_COUNT):

            try:

                print(f"TRY {i+1}")
