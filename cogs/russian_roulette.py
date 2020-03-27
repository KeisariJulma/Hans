import discord
import asyncio
import random
from logger import logger
from discord.ext import commands
players=[]
class russian_roulette(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='Join russian ruolette', aliases=['roulette'])
    async def _join_russian_roulette(self, ctx: commands.Context):
        players.append(ctx.author.id)
        await ctx.send(ctx.author.mention+'Joined to Russian roulette')

    @commands.command(name='Game of Russian ruolette', aliases=['keks'])
    async def russian_roulette(self, ctx: commands.Context):
        await ctx.send('<@'+str(random.choice(players))+'>'+' wins')
def setup(bot):
    bot.add_cog(russian_roulette(bot))
    logger.info(f'Loaded russian roulette')
