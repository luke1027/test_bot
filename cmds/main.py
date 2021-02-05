import discord
from discord.ext import commands
from core.classes import CogExtension


class Main(CogExtension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("1234")

    # https://cog-creators.github.io/discord-embed-sandbox/
    @commands.command()
    async def get(self, ctx):
        embed = discord.Embed(title="title", description="description", color=0x0056d6)
        embed.set_author(name="name",
                         icon_url="https://www.rover.com/blog/wp-content/uploads/2019/11/shiba-dreamstime-960x540.jpg")
        embed.add_field(name="1", value="11", inline=True)
        embed.add_field(name="2", value="22", inline=True)
        embed.set_footer(text="footer")
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, msg):
        # delete
        await ctx.message.delete()
        # repeat
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num + 1)


def setup(bot):
    bot.add_cog(Main(bot))
