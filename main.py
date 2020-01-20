import discord
import os
import random
import logging
import json
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from dotenv import load_dotenv
from os.path import join, dirname

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

load_dotenv(join(dirname(__file__), '.env'))
token = os.getenv('DISCORD_TOKEN')

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
'''
with open("config/config.json") as cfg:
    config = json.load(cfg)
'''

def get_prefix(bot, message):
    prefixes = [',']
    if not message.guild:
        return ','
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = Bot(command_prefix=get_prefix)

cogs = [
    'cogs.basic',
    'cogs.music.music'
]

if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id} Version: {discord.__version__}\n')
    logger.info(f'Logged in as: {bot.user.name} - {bot.user.id} Version: {discord.__version__}')


@loop(seconds=120)
async def status_change():
    await bot.wait_until_ready()
    statusses = ["Little game of gas the jew", "Keep advancing and the Soviets will fall.", "Tour de France the game"]
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=random.choice(statusses)))


status_change.start()
bot.run(token, bot=True, reconnect=True)
