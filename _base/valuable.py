from abc import ABC, abstractmethod

class ValuableABC(ABC):
    def __init__(self, analysis):
        self._analysis = analysis

    @abstractmethod
    def evaluate(self):
        pass
    
    @abstractmethod
    def explain(self):
        pass