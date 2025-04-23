from _base.bot import BotCommandsABC
import discord
from discord.ext import commands
from data.yfinance_collector import yFinanceCollector
from datetime import datetime, timedelta

class RaskolnikovBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='get_latest_data', help='Fetches latest data for a given ticker', alias=['info'])
    async def get_latest_data(self, ctx, ticker, embed):
        try:
            _yf = yFinanceCollector({
                'advantage_url':'https://www.alphavantage.co/query?function=OVERVIEW&symbol=_ticker}&apikey=_api_key'
                , 'advantage_key': 'HVT22YLBMRKMN92D'
            })
            res = _yf.get_info(ticker)
            
            if not res:
                await ctx.send(f"hmmm... I don't have any data for {ticker.upper()}")
                return

            _embed = discord.Embed(
                title = f"{res.get('shortName', ticker)} ({ticker.upper()})"
                , color = discord.Color.blue()
            )
            # fields
            _embed.add_field(name="Current Price", value=f"${res.get('currentPrice', 'N/A')}")
            _embed.add_field(name="Day High", value=f"${res.get('dayHigh', 'N/A')}")
            _embed.add_field(name="Day Low", value=f"${res.get('dayLow', 'N/A')}")
            _embed.add_field(name="52 Week High", value=f"${res.get('fiftyTwoWeekHigh', 'N/A')}")
            _embed.add_field(name="52 Week Low", value=f"${res.get('fiftyTwoWeekLow', 'N/A')}")
            
            # additional info
            _embed.set_footer(text=f"Data from Yahoo Finance • {res.get('exchange', 'Unknown Exchange')}")
            
            await ctx.send(embed=_embed)
        except Exception as e:
            await ctx.send(f"Error fetching data: {str(e)}")
