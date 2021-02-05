import discord
from discord.ext import commands
from core.classes import CogExtension
import json

with open('setting.json', 'r', encoding='utf8') as file:
    data = json.load(file)


class Event(CogExtension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(data["New_Channel"])
        await channel.send(f'{member} join!')
        print(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        print(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'apple' and msg.author != self.bot.user:
            await msg.channel.send('hi')


def setup(bot):
    bot.add_cog(Event(bot))
