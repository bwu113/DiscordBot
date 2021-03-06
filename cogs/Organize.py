import discord
from discord.ext import commands

class Organize(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def createchannel(self, ctx, channel_name):
        await ctx.guild.create_text_channel(channel_name)
        await ctx.send(f'A new text channel called {channel_name} was created.')

    @commands.command()
    async def removechannel(self, ctx, channel: discord.TextChannel):
        await channel.delete()
        await ctx.send(f'Channel {channel} was removed.')

def setup(client):
    client.add_cog(Organize(client))