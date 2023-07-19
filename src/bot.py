import os
import discord
import random
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

INTENTS = discord.Intents.default()
INTENTS.members = INTENTS.messages = INTENTS.message_content = INTENTS.dm_messages = True
client = discord.Client(intents=INTENTS)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the bot test server!!! :)'
    )

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content == "!help" or message.content == "!commands":
        res = "List of Commands : \n" 
        for command in ALL_COMMENDS:
            res += command + "\n"
        await message.channel.send(res)

    if message.content == "!luck":
        res = "Your luck today is : " + random.choice(luck)
        await message.channel.send(res)

ALL_COMMENDS = ["!help","!commands","!luck"]
luck = ["Good", "AWESOME", "Meh", "Pretty bad", "You should probably stay home"]

client.run(TOKEN)