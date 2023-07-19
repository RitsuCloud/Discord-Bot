import os
import discord
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

INTENTS = discord.Intents.default()
INTENTS.members = INTENTS.messages = INTENTS.message_content = INTENTS.dm_messages = True
INTENTS
client = discord.Client(intents=INTENTS)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    # this just displays its own name, since the bot doesn't have enough permission
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members: \n - {members}')

# doesn't quite work
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the bot test server!!! :)'
    )

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    
    cringe = "SENTINENLSSS OMG LOL"

    if message.content == "val!":
        response = cringe
        await message.channel.send(response)

    if message.author.name == "africanneo":
        await message.channel.send("Your pretty smart guy")

    print(type(message.author))

client.run(TOKEN)