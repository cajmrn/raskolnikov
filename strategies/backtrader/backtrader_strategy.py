import backtrader as bt
from backtrader.feeds import PandasData

class BacktraderSMACrossStrategy(bt.Strategy):
    def __init__(self):
        self.signal = self.data.signal

    def next(self):
        if self.signal[0] == 1:
            self.buy()
        elif self.signal[1] == -1:
            self.sell()

class BacktraderSMACrossStrategyPandasData(PandasData):
    lines = ('signal',)
    params = (('signal', 6),)