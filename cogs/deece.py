import discord
from discord.ext import commands

class Deece(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'deece' in message.content.lower() or \
            'deace' in message.content.lower() or \
            'deez' in message.content.lower() or \
            'deese' in message.content.lower() or \
            'deace' in message.content.lower():
            await message.channel.send('Nuts!')

def setup(client):
    client.add_cog(Deece(client))