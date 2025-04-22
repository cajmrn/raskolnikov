from _base.data import DataCollectorABC
import yfinance as yf
import requests

class yFinanceCollector(DataCollectorABC):
    def __init__(self, config):
        self._config = config
        self._advantage_key = ''
        self.stock = None
        self._advantage_url = ''
        self.parse_config()

    def parse_config(self):
        self._advantage_key = self._config['advantage_key']
        self._advantage_url = self._config['advantage_url']
        
    def get_historical_data(self, ticker, period='1y'):
        self.stock = yf.Ticker(ticker)
        #return self.stock.history(period=period)
        return self.stock.info
    
    def get_fundamentals(sefl, ticker):
        return requests.get(
                    _advantage_url.replace('_ticker', ticker).replace('_api_key',self._advantage_key )
                    ).json()
    def fetch_daily_data(self, symbol):
        pass
    
    def get_tracked_symbols(self):
        pass