from abc import ABC, abstractmethod

class BotCommandsABC(ABC):
    @abstractmethod
    async def recommend(self, ctx, strategy_name = 'short_term'):
        pass

    @abstractmethod
    async def analyze_portfolio(self, ctx):
        pass

    @abstractmethod
    async def set_alert(self, ctx, symbol, condition, value):
        pass
    
    @abstractmethod
    async def get_daily_info(self, ctx, symbol):
        pass