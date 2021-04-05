import discord
import asyncio
import time
import sys

bot_ids = []    #Enter your bot ids here
bot_index = -1
last_message = ""
selected_channel = ""
wait = 0
text = ""
with open("asciiframes.txt", "r") as f: #asciiframes.txt can be renamed to your text file's name
    text = f.read()
frames = text.split("`")    #Grabs individual messages from text file, split by `
count = 0
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {}#{}'.format(client.user.name, client.user.discriminator))

@client.event
async def on_message(message):
    global bot_index    #global keyword used so a separate instanced variable isn't created
    global bot_ids
    global last_message
    global frames
    global count
    global selected_channel
    global wait
    if (message.content == ".startascii"):  #Starts up the messaging
        selected_channel = message.channel
        bot_index = 0
    if (bot_index == -1):
        return
    if (message.author.id in bot_ids and bot_index == bot_ids.index(message.author.id) and bot_ids[bot_index] != client.user.id):
        if (last_message != ""):
            tl = last_message
            last_message = ""
            try:
                await tl.delete()   #When a new bot sends a message, previous bot deletes its message
            except Exception as e:
                last_message = ""
                print(e)
        if (bot_index == len(bot_ids) - 1):
            bot_index = 0
            count += 1
        else:
            bot_index += 1                
    if (bot_ids[bot_index] == client.user.id and wait == 0):
        wait = 1
        time.sleep(0.3)    #Adjust this to match the fps you want, I would advise not going lower unless you use 7+ bots
        print(str(((count * len(bot_ids)) + bot_index) % len(frames)) + ": " + str(client.user.id))
        last_message = await selected_channel.send("```" + frames[((count * len(bot_ids)) + bot_index) % len(frames)] + "```")
        wait = 0
        if (bot_index == len(bot_ids) - 1):
            bot_index = 0
            count += 1
        else:
            bot_index += 1
        return

client.run(sys.argv[1], bot=True)
