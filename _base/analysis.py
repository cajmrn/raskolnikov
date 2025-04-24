from abc import ABC, abstractmethod

class TechnicalAnalyzerABC(ABC):
    @abstractmethod
    def analyze(self, price_data):
        pass

class SentimentAnalyzerABC(ABC):
    @abstractmethod
    def analyze_text(self, text):
        pass

    @abstractmethod
    def analyze_news(self, headlines):
        pass

class PortfolioAnalyzerABC(ABC):
    @abstractmethod
    def analyze_position(self, position, market_data):
        pass

    @abstractmethod
    def generate_recommendation(self, positions):
        pass