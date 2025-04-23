from data.yfinance_collector import yFinanceCollector
from comms.raskolnikov_bot import Raskolnikov
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
_r = commands.Bot(command_prefix = '!', intents=intents)

@_r.event
async def on_ready():
    print(f'logged in as {_r.user.name} (ID: {_r.user.id})')

async def setup_bot():
    await _r.add_cog(Raskolnikov(_r))

if __name__ == "__main__":
    _yf = yFinanceCollector({
        'advantage_url':'https://www.alphavantage.co/query?function=OVERVIEW&symbol=_ticker&apikey=_api_key'
        , 'advantage_key': 'HVT22YLBMRKMN92D'
    })

    res = _yf.get_historical_data('AAPL')

    fund = _yf.get_fundamentals('AAPL')
    print(fund)
    # print(res)
    # import asyncio
    # asyncio.run(setup_bot())
    # _r.run('') #todo incorporate env loading for key
