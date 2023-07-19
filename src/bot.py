import os
import discord
import random
from discord import Intents
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

INTENTS = discord.Intents.default()
INTENTS.members = INTENTS.messages = INTENTS.message_content = INTENTS.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=INTENTS)

@bot.event
async def on_ready():
    print("Bot is READY!!!")

@bot.command(name="commands", help="This prints out the list of avaiable commands")
async def print_commands(ctx):
    res = "List of Commands : \n" 
    for command in ALL_COMMENDS:
        res += command + "\n"
    await ctx.send(res)

@bot.command(name="luck", help="This tells you your luck for the day!")
async def luck_today(ctx):
    res = "Your luck today is : " + random.choice(luck)
    await ctx.send(res)

@bot.event
async def on_message(message):
    if "fuck" in message.content:
        await message.channel.send("NO CURSING") 

ALL_COMMENDS = ["!help","!commands","!luck"]
luck = ["Good", "AWESOME", "Meh", "Pretty bad", "You should probably stay home"]

bot.run(TOKEN)