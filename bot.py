import discord
from discord.ext import commands
import json
import os

with open('setting.json', 'r', encoding='utf8') as file:
    data = json.load(file)

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print('>> Bot is online. <<')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done.')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done.')


for filename in os.listdir('cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(data["TOKEN"])
