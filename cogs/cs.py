    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.guild_only()
    @commands.has_role('SS-Oberführer')
    @commands.command(
        name='seturiminzokkiri',
        description='Sets music channel'
    )
    async def setmusic(self, ctx):
        try:
            config[str(ctx.guild.id)]['uriminzokkiri'] = ctx.channel.id
        except KeyError:
            config[str(ctx.guild.id)] = {}
            config[str(ctx.guild.id)]['uriminzokkiri'] = ctx.channel.id
        config.write()
        await ctx.send("uriminzokkiri channel set!")


    @loop(seconds=120)
    async def senduriminzokkiri():
        bot = Bot(command_prefix=get_prefix)
        channels = []
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
                    await bot.get_channel(channel).send(link)

        del links_with_text
        del channels
