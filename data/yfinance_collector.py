from _base.data import DataCollectorABC
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr

class yFinanceCollector(DataCollectorABC):
    def __init__(self, config=None):
        self._config = config
        self._stock = None
        self._df = pd.DataFrame()
        self.parse_config()

    def parse_config(self):
        pass

    def set_stock(self, ticker, period='1y'):
        self._stock = yf.Ticker(ticker)
        return self._stock

    def get_info(self):
        return self._stock.info

    def download(self, symbol, period='30d', interval='1h', progress=False):
        self._df = yf.download(
            tickers=symbol
            , period=period  # Make sure to use keyword arguments
            , interval=interval
            , progress=progress
        )
        return self._df

    def get_history(self, period='1d'):
        return self._stock.history(period)

    def get_close(self):
        return self.get_history()['Close'].iloc[-1]
    
    def pe_ratio(self):
        return self.get_info().get('trailingPE', None)

    def price_to_book(self):
        return self.get_info().get('priceToBook', None)

    def mean_cashflow(self):
        return self._stock.cashflow.loc['Free Cash Flow'].mean()

    def bond_yield(self):
        return pdr.get_data_fred('DGS10').iloc[-1,0] / 100

    def dcf(self):
        fcf = self.mean_cashflow()
        growth_rate = 0.05
        discount_rate = self.bond_yield() + 0.05

        return (fcf * (1 + growth_rate)) / (discount_rate - growth_rate)

    def eps(self):
        return self.get_info().get('trailingEps', None)
    
    def get_balance_sheet(self):
        return self._stock.balance_sheet

    def total_stockholder_equity(self):
        return self.get_balance_sheet().loc['Stockholders Equity'].iloc[0]

    def shares_outstanding(self):
        return self.get_info().get('sharesOutstanding', None)

    def book_value(self):
        return self.total_stockholder_equity() / self.shares_outstanding()

    def graham_value(self):
        return (22.5 * self.eps() * self.book_value()) ** 0.5 if self.eps() else None

    def earnings_yield(self):
        return (self.eps() / self.get_close()) * 100 if self.eps() else None

    def enterprise_value(self):
        return self.get_info().get('enterpriseValue', None)

    def get_income_statement(self):
        return self._stock.income_stmt

    def ebitda(self):
        return self.get_income_statement().loc['EBITDA'].iloc[0] if 'EBITDA' in self.get_income_statement().index else None

    def ev_ebitda(self):
        return self.enterprise_value() / self.ebitda() if self.ebitda() else None
    
    def get_tracked_symbols(self):
        pass