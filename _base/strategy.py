from abc import ABC, abstractmethod

class TradingStrategyABC(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
    
    @property
    @abstractmethod
    def description(self):
        pass
    
    @abstractmethod
    def calculate_features(self, symbol, data,):
        pass
    
    @abstractmethod
    def generate_signals(self, symbol, data):
        pass

class StrategyConfig:
    def __init__(self, params=None, data_params=None):
        self.params = params or {}
        self.data_params = data_params or {}

class StrategyFactoryABC(ABC):
    @abstractmethod
    def get_strategy(self, name: str):
        pass

    @abstractmethod
    def list_strategies(self):
        pass