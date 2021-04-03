import discord
from discord.ext import commands

#Character used before a command
entryBot = commands.Bot(command_prefix='.')

def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

@entryBot.event
async def on_ready():
    print('Bot is ready.')

@entryBot.event
async def on_voice_state_update(member, before, after):
    channel = after.channel
    if after.channel.id is not None and member.id == 180933850476707840:
        await channel.connect()
        await member.guild.voice_client.play(discord.FFmpegPCMAudio('sound.mp3',executable="D:/Discord Bot/ffmpeg/bin/ffmpeg.exe"),after=await member.guild.voice_client.disconnect())

entryBot.run(token)