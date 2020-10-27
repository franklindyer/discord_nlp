import discord
from discord.ext import commands
import sys
import requests
import os
import markovify

description = "Do robo-platonists dream of electric forms?"

intents = discord.Intents.default()
intents.members = True

TEXT_MODELS = {}
texts = os.listdir('corpus/')
for t in texts:
    f = open('corpus/' + t, 'r')
    TEXT_MODELS[t] = markovify.Text(f, state_size=2) 

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

@bot.command()
async def imitate(ctx, person):
    if person + '.txt' in TEXT_MODELS:
        await ctx.send(TEXT_MODELS[person + '.txt'].make_sentence(tries=100))
    else:
        await("Sorry, I don't know anyone by that name.")

bot.run(sys.argv[1])
