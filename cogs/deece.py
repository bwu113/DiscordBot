import discord
from discord.ext import commands

class Deece(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'deece'.lower() in message.content:
            await message.channel.send('Nuts!')


def setup(client):
    client.add_cog(Deece(client))