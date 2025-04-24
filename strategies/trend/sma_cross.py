from dataclasses import dataclass
from _base.strategy import TradingStrategyABC, StrategyConfig
import pandas as pd

class SmaCrossStrategy(TradingStrategyABC):
    def __init__(self, config=None):
        print("SmaCrossSTrategy:", config)
        self._config = config or StrategyConfig(
            params={'fast_period': 10, 'slow_period': 30}
        )
    
    @property
    def name(self):
        return "SMACross"
    
    @property
    def description(self):
        return (f"{self._config.params['fast_period']}/{self._config.params['slow_period']} "
                f"SMA Crossover Strategy")
    
    def calculate_features(self, symbol, data):
        """Compute SMA indicators"""
        p = self._config.params
        print("config", p)
        data['SMA_Fast'] = data[('Close', symbol)].rolling(p['fast_period']).mean()
        data['SMA_Slow'] = data[('Close', symbol)].rolling(p['slow_period']).mean()
        return data
    
    def generate_signals(self, symbol, data):
        """Generate trading signals (1=long, -1=short, 0=neutral)"""
        if 'SMA_Fast' not in data.columns:
            data = self.calculate_features(symbol, data)
        
        signals = pd.Series(0, index=data.index)  # Default neutral
        signals[data['SMA_Fast'] > data['SMA_Slow']] = 1   # Long when fast > slow
        signals[data['SMA_Fast'] < data['SMA_Slow']] = -1  # Short when fast < slow
        return signals