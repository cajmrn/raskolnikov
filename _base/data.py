from abc import ABC, abstractmethod

class DataCollectorABC(ABC):
    @abstractmethod
    def get_info(self, symbols) :
        pass

    @abstractmethod
    def get_tracked_symbols(self) :
        pass

class DataStorageABC(ABC):
    @abstractmethod
    def save_daily_data(self, symbol, data):
        pass

    @abstractmethod
    def get_historical_data(self, symbo, days):
        pass