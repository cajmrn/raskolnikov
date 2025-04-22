from abc import ABC, abstractmethod
from typing import Dict, Tuple

class TechnicalAnalyzerABC(ABC):
    @abstractmethod
    def analyze(self, price_data: Dict) -> Dict[str, float]:
        pass

class SentimentAnalyzerABC(ABC):
    @abstractmethod
    def analyze_text(self, text: str) -> float:
        pass

    @abstractmethod
    def analyze_news(self, headlines: List[str]) -> float:
        pass

class PortfolioAnalyzerABC(ABC):
    @abstractmethod
    def analyze_position(self, position: Dict, market_data: Dict) -> Dict:
        pass

    @abstractmethod
    def generate_recommendation(self, positions: List[Dict]) -> List[Dict]:
        pass