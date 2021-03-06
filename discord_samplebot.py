import discord
from discord.ext import commands
import sys
import requests

description = "Just a humble sample bot. Aims to please."

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print('~~ Logged in ~~')

@bot.command()
async def parrot(ctx, repeat: int, message="squawk!"):
    for i in range(0, repeat):
        await ctx.send(message)

@bot.command()
async def wikipedia(ctx):
    r = requests.get("https://en.wikipedia.org/wiki/special:random")
    await ctx.send(r.url)

bot.run(sys.argv[1])
