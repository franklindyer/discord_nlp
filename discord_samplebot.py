import discord
from discord.ext import commands
import sys

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

bot.run(sys.argv[1])
