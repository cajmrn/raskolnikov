from abc import ABC, abstractmethod
from typing import Dict, List

class BotCommandsABC(ABC):
    @abstractmethod
    async def recommend(self, ctx, strategy_name: str = 'short_term'):
        pass

    @abstractmethod
    async def analyze_portfolio(self, ctx):
        pass

    @abstractmethod
    async def set_alert(self, ctx, symbol: str, condition: str, value: float):
        pass
    
    @abstractmethod
    async def get_daily_info(self, ctx, symbol: str):
        pass