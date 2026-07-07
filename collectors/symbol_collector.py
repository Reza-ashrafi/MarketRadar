import pandas as pd
from datetime import datetime

from collectors.tsetmc_client import TSETMCClient
from config.settings import SYMBOL_DIR


class SymbolCollector:

    def __init__(self):
        self.client = TSETMCClient()

    def collect(self):
        """
        دریافت لیست نمادهای بازار
        """

        url = (
            "https://cdn.tsetmc.com/api/Instrument/GetInstrumentInfo"
        )

        data = self.client.get(url)

        print("TSETMC data received")

        return data
