import discord
import requests
import json
from discord.ext import commands

class FF14(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def search(self, ctx, *, itemName):
        worldList = ['Adamantoise', 'Cactuar', 'Faerie', 'Gilgamesh', 'Jenova', 'Midgardsormr', 'Sargatanas', 'Siren']
        response = requests.get(f'https://xivapi.com/search?string={itemName}')
        result = json.loads(response.text)

        if result == "":
            return await ctx.send("No results are found for \ " + itemName + "\, Are you sure you spelled the name correctly?")

        itemID = ''
        itemIcon = ''
        for info in result['Results']:
            if info['Name'].lower() == itemName.lower():
                itemID = info['ID']
                itemIcon = info['Icon']

        for world in worldList:
            response = requests.get(f'https://universalis.app/api/{world}/{itemID}')
            result = json.loads(response.text)
            embed = discord.Embed(title="title", description="description", color=0x527dff)
            embed.set_author(name=f'{world}')
            embed.set_thumbnail(url=f'https://xivapi.com/{itemIcon}')
            embed.add_field(name="Retainer", value=result['listings'][0]['retainerName'], inline=True)
            embed.add_field(name="Quantity ", value=result['listings'][0]['quantity'], inline=True)
            embed.add_field(name="Unit Price", value=result['listings'][0]['pricePerUnit'], inline=True)
            embed.add_field(name="Total Cost", value=result['listings'][0]['total'], inline=True)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(FF14(client))