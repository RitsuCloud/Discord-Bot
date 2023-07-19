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

ALL_COMMENDS = ["!help","!commands","!luck", "!roll"]
luck = ["Good", "AWESOME", "Meh", "Pretty bad", "You should probably stay home"]
greetings = ["Hi, Hello"]

@bot.event
async def on_ready():
    print("Bot is READY!!!")

@bot.listen("on_message")
async def on_message_listen(message):
    if "Hi" in message.content:
        await message.channel.send("Hello :)")

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
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):       
        await ctx.send("Not a valid command. !commands to see a list of commands!")

@bot.command(name="roll", help="Roll to see if you can beat the bot :)")
async def roll_battle(ctx):
    bot_roll = random.randrange(1, 13)
    player_roll = random.randrange(1, 13)
    if bot_roll > player_roll:
        res = "You lose :) \n"
    elif bot_roll < player_roll:
        res = "You win :( \n"
    else:
        res ="Is a draw "
    await ctx.send(res + (f'Your roll: {player_roll} Bot roll: {bot_roll}'))

bot.run(TOKEN)