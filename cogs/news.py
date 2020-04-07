# -*- coding: utf-8 -*-
import asyncio
import discord
from discord.ext import commands
from logger import logger
from configobj import ConfigObj
import requests
from bs4 import BeautifulSoup
from discord.ext.commands import Bot
from discord.ext.tasks import loop

config = ConfigObj('conf.ini')
import functools
import itertools


class News(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.senduriminzokkiri.start()

    @loop(seconds=120)
    async def senduriminzokkiri(self):
        channels = ['630668359293468682']
        with open('send.txt') as f:
            send = f.readlines()
        send = [x.strip() for x in send]
        with open('conf.ini') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for line in content:
            if 'uriminzokkiri' in line:
                channels.append(line.split("= ",1)[1])
        links_with_text = [a['href'] for a in BeautifulSoup(requests.get('http://www.uriminzokkiri.com/index.php?lang=eng&ptype=cfonew').content, 'lxml').find_all('a', href=True) if 'index.php?ptype=cfonew&lang=eng&mtype=view&no=' in a['href']]
        for link in reversed(links_with_text):
            if link not in send:
                with open('send.txt', 'w') as sendfile:
                    sendfile.write(link+'\n')
                for channel in channels:
                    print (channel)
                    await self.bot.get_channel(channel).send(link)

        del links_with_text
        del channels


def setup(bot):
    bot.add_cog(News(bot))
    logger.info(f'Loaded News')
