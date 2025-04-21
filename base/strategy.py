from abc import ABC, abstractmethod
from typing import Dict

class TradingStrategyABC(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def analyze(self, symbol_data: Dict) -> Dict:
        pass

class StrategyFactoryABC(ABC):
    @abstractmethod
    def get_strategy(self, name: str) -> TradingStrategyABC:
        pass

    @abstractmethod
    def list_strategies(self) -> List[str]:
        pass