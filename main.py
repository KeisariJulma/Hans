# -*- coding: utf-8 -*-
import os
import random
import sys
from shutil import move
from time import sleep
from discord import __version__
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from dotenv import load_dotenv
from os.path import join, dirname
move(join(os.getcwd(),'discord.log'), os.getcwd()+'\\logs\\')
from logger import logger
from threading import Thread
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
    'cogs.music.music'
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


def restart():
    print('start')
    sleep(86400)
    os.system('pip install -U discord.py[voice] pynacl youtube-dl --upgrade')
    os.execv(sys.executable, ['python'] + sys.argv)


def main():
    for cog in cogs:
        bot.load_extension(cog)
    t = Thread(target = restart)
    t.daemon = True
    t.start()
    status_change.start()
    bot.run(token, bot=True, reconnect=True)


if __name__ == '__main__':
    main()
