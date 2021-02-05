import discord
from discord.ext import commands
from core.classes import CogExtension
import random
import json

with open('./setting.json', 'r', encoding='utf8') as file:
    data = json.load(file)


class React(CogExtension):
    pass
    @commands.command()
    async def img(self, ctx):
        random_pic = random.choice(data["pic"])
        # pic = discord.File(random_pic)
        await ctx.send(random_pic)


def setup(bot):
    bot.add_cog(React(bot))
