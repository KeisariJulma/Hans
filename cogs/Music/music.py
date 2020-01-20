from discord.ext import commands
from datetime import datetime as d

# New - The Cog class must extend the commands.Cog class
class Music(commands.Cog):
    

def setup(bot):
    bot.add_cog(Music(bot))
