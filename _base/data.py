from abc import ABC, abstractmethod
from typing import Dict, List, Any

class DataCollectorABC(ABC):
    @abstractmethod
    def fetch_daily_data(self, symbols: List[str]) -> Dict[str, Dict]:
        pass

    @abstractmethod
    def get_tracked_symbols(self) -> List[str]:
        pass

class DataStorageABC(ABC):
    @abstractmethod
    def save_daily_data(self, symbol: str, data: Dict):
        pass

    @abstractmethod
    def get_historical_data(self, symbol: str, days: int) -> Dict:
        pass