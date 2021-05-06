import discord
from discord.ext import commands

class Organize(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def channel(self, ctx, channel_name):
        await ctx.guild.create_text_channel(channel_name)
        await ctx.send(f'A new text channel called {channel_name} was created.')

def setup(client):
    client.add_cog(Organize(client))