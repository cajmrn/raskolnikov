from _base.data import DataCollectorABC
import yfinance as yf
import pandas as pd

class yFinanceCollector(DataCollectorABC):
    def __init__(self, config=None):
        self._config = config
        self._stock = None
        self._df = pd.DataFrame()
        self.parse_config()

    def parse_config(self):
        pass
        
    def get_info(self, ticker, period='1y'):
        self._stock = yf.Ticker(ticker)
        #return self.stock.history(period=period)
        return self._stock.info

    def download(self, symbol, period='30d', interval='1h', progress=False):
        self._df = yf.download(
            tickers=symbol
            , period=period  # Make sure to use keyword arguments
            , interval=interval
            , progress=progress
        )
        return self._df        
    
    def get_tracked_symbols(self):
        pass