import discord
import io
import matplotlib.pyplot as plt

from discord.ext import commands
from _base.bot import BotCommandsABC
from strategies import StrategyFactory
from datetime import datetime, timedelta
from analysis.valuator import TechnicalValuator
from ext_discord.discord_embed import EmbedTemplate
from data.yfinance_collector import yFinanceCollector
from strategies.backtest_runner import BacktraderAdapter
from strategies.backtrader.backtrader_strategy import BacktraderSMACrossStrategy

class RaskolnikovBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='get_latest_data', help='Fetches latest data for a given ticker', aliases=['info'])
    async def get_latest_data(self, ctx, ticker, embed=None):
        try:
            # todo refactor Collector 
            _yf = yFinanceCollector()
            res = _yf.set_stock(ticker)
            info = res.get_info()
            
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

    @commands.command(name='sim_smacross', help='takes initial cash and sims with smacross', aliases=['sma'])
    async def sim_smacross(self, ctx, ticker, initial_cash, embed=None):
        try:
            _yf = yFinanceCollector()
            _df = _yf.download(ticker)

            factory = StrategyFactory()
            smacross = factory.create_strategy('smacross', None)
            _initial_cash = initial_cash
            cerebro, results =  BacktraderAdapter.run_backtest(
                symbol = ticker
                , signal_strategy = smacross
                , bt_strategy = BacktraderSMACrossStrategy
                , ohlc_data = _df
                , initial_cash = _initial_cash
            )

            if not results and cerebro:
                await ctx.send(f"hmmm... something went wrong {ticker.upper()}")
                return

            plt_res = cerebro.plot()
            fig = plt_res[0][0]

            buffer = io.BytesIO()
            fig.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
            buffer.seek(0)

            _embed = discord.Embed(
                title = f"SIMMED: {ticker.upper()}"
                , color = discord.Color.blue()
            )
            # fields
            file = discord.File(buffer, filename="backtest_plot.png")

            _embed.add_field(name="INITIAL CASH", value=f"${_initial_cash}")
            _embed.add_field(name="Day High", value=f"${cerebro.broker.getvalue()}")
            _embed.set_image(url='attachment://backtest_plot.png')
            # additional info
            _embed.set_footer(text=f"Raskolnikov says: Not finiancical advice")
            
            await ctx.send(embed=_embed)
            buffer.close()
            plt.close(fig)

        except Exception as e:
            await ctx.send(f"Error fetching data: {str(e)}")

    @commands.command(name='valuation', help='valuates the Stock as valued or undervalued', aliases=['value'])
    async def valuation(self, ctx, ticker, embed=None):
        try:
            _tv = TechnicalValuator(yFinanceCollector(), ticker)
            _a = _tv.analyze()

            _et = EmbedTemplate.get_valuation_info(ticker=ticker, data=_a)
            
            await ctx.send(embed=_et.create_embed())
        except Exception as e:
            await ctx.send(f"Error analyzing {ticker.upper()}: {str(e)}")


    @commands.command(name='release_notes', help='release notes', aliases=['release'])
    async def release_notes(self, ctx, ticker, embed=None):
        try:
            _embed = discord.Embed(
                title = f"Raskolikov_v0.005"
                , color = discord.Color.blue()
            )

            _embed.add_field(name="2025-04-21", value=f" - Birth")
            _embed.add_field(name="2025-04-22", value=f" - Discord integration")
            _embed.add_field(name="2025-04-23", value=f" - get_latest_data functionality")
            _embed.add_field(name="2025-04-24", value=f" - smscross functionality")
            _embed.add_field(name="2025-05-01", value=f" - valuation functionality")

            # additional info
            _embed.set_footer(text=f"Raskolnikov says: Not finiancical advice")

        except Exception as e:
            await ctx.send(f"Error analyzing {ticker.upper()}: {str(e)}")
    
    
