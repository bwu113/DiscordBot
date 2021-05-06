import discord
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events go in Cog.Listener
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    # Commands go in here
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong')

def setup(client):
    client.add_cog(Music(client))


#@entryBot.event
#async def on_voice_state_update(member, before, after):
 #   channel = after.channel
  #  if after.channel.id is not None and member.id == 180933850476707840:
   #     await channel.connect()
    #    await member.guild.voice_client.play(discord.FFmpegPCMAudio('sound.mp3',executable="D:/Discord Bot/ffmpeg/bin/ffmpeg.exe"),after = disconnect(member))

#async def disconnect(member):
 #   await asyncio.sleep(2)
  #  await member.guild.voice_client.disconnect()