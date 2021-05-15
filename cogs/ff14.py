import asyncio

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
        try:
            response = requests.get(f'https://xivapi.com/search?string={itemName}')
            result = json.loads(response.text)
        except:
            return await ctx.send("No results are found for " + itemName + ", Are you sure you spelled the name correctly?")

        itemID = ""
        itemIcon = ""
        itemTrueName = ""
        current = 0
        content = []

        for info in result['Results']:
            if info['Name'].lower() == itemName.lower():
                itemID = info['ID']
                itemIcon = info['Icon']
                itemTrueName = info['Name']
                break

        for world in worldList:
            try:
                response = requests.get(f'https://universalis.app/api/{world}/{itemID}')
                result = json.loads(response.text)
            except:
                continue
            embed = discord.Embed(title=itemTrueName, description="", color=0x527dff)
            embed.set_image(url=f'https://xivapi.com/{itemIcon}')
            embed.add_field(name="Retainer", value=result['listings'][0]['retainerName'], inline=True)
            embed.add_field(name="Unit Price", value=result['listings'][0]['pricePerUnit'], inline=True)
            embed.add_field(name="Total Cost", value=result['listings'][0]['total'], inline=True)
            embed.add_field(name="Quantity", value=result['listings'][0]['quantity'], inline=True)
            embed.add_field(name="Server", value=world, inline=True)
            content.append(embed)

        for items in range(len(content)):
            content[items].set_footer(text=f'Page: {items+1}/{len(content)}')
        buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]
        message = await ctx.send(embed=content[current])

        for reactions in buttons:
            await message.add_reaction(reactions)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in buttons

        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=10, check=check)

                if reaction.emoji == buttons[0] and current != 0:
                    current = 0
                    await message.edit(embed=content[current])
                    await message.remove_reaction(reaction, user)

                if reaction.emoji == buttons[3] and current != len(content)-1:
                    current = len(content)-1
                    await message.edit(embed=content[current])
                    await message.remove_reaction(reaction, user)

                if reaction.emoji == buttons[1] and current != 0:
                    current -= 1
                    await message.edit(embed=content[current])
                    await message.remove_reaction(reaction, user)
                elif reaction.emoji == buttons[1] and current == 0:
                    current = len(content)-1
                    await message.edit(embed=content[current])
                    await message.remove_reaction(reaction, user)
                elif reaction.emoji == buttons[2] and current != len(content)-1:
                    current += 1
                    await message.edit(embed=content[current])
                    await message.remove_reaction(reaction, user)
                elif reaction.emoji == buttons[2] and current == len(content)-1:
                    current = 0
                    await message.edit(embed=content[current])
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                await message.delete()
                await ctx.message.delete()
                return


def setup(client):
    client.add_cog(FF14(client))