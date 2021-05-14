import discord
from discord.ext import commands

class FF14(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def search(self, ctx, world, *, item):
        await ctx.send('It works' + world + '|' + item)

def setup(client):
    client.add_cog(FF14(client))