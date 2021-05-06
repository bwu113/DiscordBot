import discord
import os
from discord.ext import commands

#Character used before a command
entryBot = commands.Bot(command_prefix='.')

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