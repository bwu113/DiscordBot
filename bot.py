import discord
import os
from discord.ext import commands

#Character used before a command
entryBot = commands.Bot(command_prefix='.')

def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

@entryBot.command()
async def load(ctx, extension):
    entryBot.load_extension(f'cogs.{extension}')

@entryBot.command()
async def unload(ctx, extension):
    entryBot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        entryBot.load_extension(f'cogs.{filename[:-3]}')

entryBot.run(os.environ['Token'])