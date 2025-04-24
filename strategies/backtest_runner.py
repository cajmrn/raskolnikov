import backtrader as bt
from strategies.backtrader.backtrader_strategy import BacktraderSMACrossStrategyPandasData

class BacktraderAdapter:
    @staticmethod
    def run_backtest(
        symbol
        , signal_strategy
        , bt_strategy
        , ohlc_data
        , initial_cash= 10000.0
        , commission= 0.001
    ):
        signals = signal_strategy.generate_signals(symbol.upper(), ohlc_data.copy())

        bt_data = ohlc_data.copy()
        bt_data.columns = bt_data.columns.get_level_values(-2)
        bt_data['signal'] = signals
        data_feed = BacktraderSMACrossStrategyPandasData(
            dataname=bt_data
            , datetime=None
            , open='Open'
            , high='High'
            , low='Low'
            , close='Close'
            , volume='Volume'
            , signal='signal'
        )
        """Converts generic signals to Backtrader execution"""
        cerebro = bt.Cerebro()
        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=commission)
        
        cerebro.adddata(data_feed)
        
        # Add strategy
        cerebro.addstrategy(bt_strategy)
        
        # Run backtest
        results = cerebro.run()
        return cerebro, results