import os
import discord
import random
from discord import Intents
from dotenv import load_dotenv
from discord.ext import commands

counts = 0

# key: users name, value: money
user_data = {}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

INTENTS = discord.Intents.default()
INTENTS.members = INTENTS.messages = INTENTS.message_content = INTENTS.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=INTENTS)

ALL_COMMENDS = ["!help","!commands","!luck", "!roll", "!adventure", "!fortune"]
luck = ["Go buy a lottery ticket","Meh", "Good", "AWESOME", "Yikes", "Pretty bad", "You should probably stay home"]
fortune = ["Today will be filled with joy and laughter.",
            "A pleasant surprise awaits you today.",
            "You might face some challenges, but remember, you're strong enough to overcome them.",
            "Luck is on your side today. Take a risk!",
            "It's a day for new beginnings. Embrace change.",
            "Your creative energy will be at its peak today.",
            "You'll meet someone special who'll leave a lasting impression.",
            "A long-desired goal may finally come to fruition today.",
            "Take some time for self-care and relaxation.",
            "You might receive unexpected financial gains."]
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

@bot.command(name="adventure", help="Comming Soon")
async def start_adventure(ctx):
    await ctx.send("Adventure game coming soon!")

@bot.command(name="fortune", help="Fortunte cookie type thing")
async def fortunte(ctx):
    res = random.choice(fortune)
    await ctx.send(res)

# this for testing purposes, will be deleted 
@bot.command(name="count")
async def count(ctx):
    global counts 
    counts += 1
    res = (f'{counts}')
    await ctx.send(res)

@bot.command(name="test")
async def test(ctx):
    res = f'{ctx.author.name}'
    await ctx.send(res)

@bot.command(name="register", help="register to start the GAMBA")
async def registerPlayer(ctx):
    if ctx.author.name in user_data:
        await ctx.send("You have already registered")
    else:
        user_data[ctx.author.name] = 1000
        if ctx.author.name in user_data and user_data[ctx.author.name] == 1000:
            await ctx.send(f'{ctx.author.name} is in you have 1000 credits')

@bot.command(name="gamba", help="Enter the amount following the command with a space")
async def gamba(ctx):
    if not ctx.author.name in user_data:
        await ctx.send("Please do !register command to get started")
    else:
        amount = ctx.message.content[len("gamba") + 2 :]
        await ctx.send(f'You tried to gamba {amount}')

@bot.command(name="check", help="Check how much user has left to gamba")
async def check_amount(ctx):
    if not ctx.author.name in user_data:
        await ctx.send("Please do !register command to get started")
    else:
        res = f'{user_data[ctx.author.name]}'
        await ctx.send(f'Amount you have: {res}')

bot.run(TOKEN)