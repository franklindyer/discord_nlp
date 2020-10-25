from discord.ext.commands import Bot
import time, asyncio
import markovify
import re
import sys

TOKEN = sys.argv[1]
client = Bot(command_prefix="$")

client.HISTORY_LIMIT = 20000
client.RE_STRING = '^[a-zA-Z0-9\s\.,“”!\?/\(\)]+$'
client.WORKING_HISTORIES = {}
client.TEXT_MODELS = {}

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    ## await message.channel.send("I heard you! {0.name}".format(message.channel))
    if message.content == '$gather':
        client.WORKING_HISTORIES[message.guild] = await message.channel.history(limit=client.HISTORY_LIMIT).flatten()
        ## await message.channel.send("Messages gathered successfully!")
        fulltext = ''
        for m in client.WORKING_HISTORIES[message.guild]: 
            if re.match(client.RE_STRING, m.content) and not m.author == client.user: 
                fulltext += m.content + '\n'
        client.TEXT_MODELS[message.guild] = markovify.NewlineText(fulltext, state_size=2)
        print("Done!")
        ## await message.channel.send("Markov model generated!")
    if re.match('^\$gather user=.+#[1-9]{4}$', message.content):
        target_username = re.match('^\$gather user=(.+)#[1-9]{4}$', message.content)[1]
        print("Conducting message scrape on user " + target_username + "...")
        client.WORKING_HISTORIES[message.guild] = await message.channel.history(limit=client.HISTORY_LIMIT).flatten()
        fulltext = ''
        tick = 0
        for m in client.WORKING_HISTORIES[message.guild]:
            if re.match(client.RE_STRING, m.content) and m.author.name == target_username: 
                fulltext += m.content + '\n'
                tick += 1
        print(tick)
        client.TEXT_MODELS[message.guild] = markovify.NewlineText(fulltext, state_size=2)
        print("Done!") 
    if re.match('^\$imitate.*', message.content):
        prompt = None
        imitation = client.TEXT_MODELS[message.guild].make_sentence(tries=500)
        print(imitation)
        if imitation:
            await message.channel.send(imitation)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
##    await start()
    while True:
        currentTime = time.strftime("%M%S", time.gmtime(time.time()))
        if currentTime == "30:00":
            await start()
        await asyncio.sleep(1)


## async def start():
##    mainChannel = client.get_channel("753724929328808009")
##    print(mainChannel.name)
##    await client.send_message(mainChannel, "Starting countdown", tts = True)



client.run(TOKEN)
