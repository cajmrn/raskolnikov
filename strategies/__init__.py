from _base.strategy import StrategyFactoryABC, StrategyConfig
from strategies.trend.sma_cross import SmaCrossStrategy

class StrategyFactory:
    _registry = {
        'smacross': SmaCrossStrategy
    }
    
    @classmethod
    def create_strategy(cls, strategy_name, config=None):
        strategy_class = cls._registry.get(strategy_name.lower())
        if not strategy_class:
            raise ValueError(f"Unknown strategy: {strategy_name}")
        if config is None:
            # Let the strategy use its own default config
            return strategy_class()
        else:
            # Pass the config through StrategyConfig
            return strategy_class(StrategyConfig(config))
    
    @classmethod
    def list_strategies(cls):
        return {name: cls._registry[name]().description 
                for name in cls._registry}