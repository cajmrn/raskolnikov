from abc import ABC, abstractmethod

class PipelineABC(ABC):
    def __init__(
        self
        , collector
        , analyzer
        , bot
        )
        self._collector = collector
        , self._analyzer = analyzer
        , self._bot = bot

    @abstractmethod
    def collect(self):
        pass

    @abstractmethod
    def analyze(self):
        pass 

    @abstractmethod
    def send(self):
        pass
        