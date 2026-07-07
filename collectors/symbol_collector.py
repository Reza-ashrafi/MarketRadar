from collectors.tsetmc_client import TSETMCClient


class SymbolCollector:

    def __init__(self):
        self.client = TSETMCClient()


    def collect(self):

        print("SYMBOL COLLECT START")

        url = "https://google.com"

        print("REQUEST URL READY")

        response = self.client.get(url)

        print("RESPONSE RECEIVED")

        return response
