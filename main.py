from data.yfinance_collector import yFinanceCollector
from strategies import StrategyFactory
from strategies.backtest_runner import BacktraderAdapter
from strategies.backtrader.backtrader_strategy import BacktraderSMACrossStrategy
from analysis.valuator import TechnicalValuator

from comms.raskolnikov_bot import RaskolnikovBot
import discord
from discord.ext import commands

# intents = discord.Intents.default()
# intents.message_content = True
# _r = commands.Bot(command_prefix = '!', intents=intents)

# @_r.event
# async def on_ready():
#     print(f'logged in as {_r.user.name} (ID: {_r.user.id})')

# async def setup_bot():
#     await _r.add_cog(Raskolnikov(_r))

if __name__ == "__main__":

    yf = yFinanceCollector()
    yf.set_stock('AAPL')

    
    #print(yf.mean_cashflow())

    _tv = TechnicalValuator(yFinanceCollector(), 'AAPL')

    _a = _tv.analyze()

    print(_a)
    
    # # res = _yf.get_info('AAPL')
    # print(res)
    # _df = _yf.download('AAPL')
    # print(_df.columns)

    # factory = StrategyFactory()
    # smacross = factory.create_strategy('smacross', None)

    # #signals = smscross.generate_signals('AAPL',_df.copy())
    # #bt_strategy = BacktraderSMACrossStrategy()

    # #print(signals)
    # initial_cash = 10000.0

    # cerebro, results =  BacktraderAdapter.run_backtest(
    #     symbol = 'AAPL'
    #     , signal_strategy = smacross
    #     , bt_strategy = BacktraderSMACrossStrategy
    #     , ohlc_data = _df
    #     , initial_cash = initial_cash
    # )

    # print(f'INITIAL CASH: {initial_cash}')
    # print(f'Value: {cerebro.broker.getvalue()}')

    # import asyncio
    # asyncio.run(setup_bot())
    # _r.run('') #todo incorporate env loading for key
