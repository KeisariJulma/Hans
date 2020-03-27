# -*- coding: utf-8 -*-
import os
import random
from discord import __version__
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from dotenv import load_dotenv
from os.path import join, dirname
from logger import logger

load_dotenv(join(dirname(__file__), '.env'))
token = os.getenv('DISCORD_TOKEN')

def get_prefix(bot, message):
    prefixes = [',']
    if not message.guild:
        return ','
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = Bot(command_prefix=get_prefix)

cogs = [
    'cogs.basic',
    'cogs.music.music',
    'cogs.russian_roulette',
    'cogs.news'
]

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id} Version: {__version__}\n')
    logger.info(f'Logged in as: {bot.user.name} - {bot.user.id} Version: {__version__}')


@loop(seconds=120)
async def status_change():
    await bot.wait_until_ready()
    statusses = ["Little game of gas the jew", "Keep advancing and the Soviets will fall", "Tour de France the game", "Russian roulette on railway platform at Birkenau"]
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=random.choice(statusses)))

def main():
    for cog in cogs:
        bot.load_extension(cog)
    status_change.start()
    bot.run(token, bot=True, reconnect=True)


if __name__ == '__main__':
    main()
