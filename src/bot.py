import os
import discord
import random
from discord import Intents
from dotenv import load_dotenv
from discord.ext import commands
import gamba as gambaGame

# key: users name, value: money
user_data = {}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

INTENTS = discord.Intents.default()
INTENTS.members = INTENTS.messages = INTENTS.message_content = INTENTS.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=INTENTS)

luck = ["Go buy a lottery ticket","Meh", "Good", "AWESOME", "Yikes", "Pretty bad", "You should probably stay home"]

@bot.event
async def on_ready():
    print("Bot is READY!!!")

@bot.listen("on_message")
async def on_message_listen(message):
    if "Hi" in message.content:
        await message.channel.send("Hello :)")

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

@bot.command(name="register", help="register to start the GAMBA")
async def registerPlayer(ctx):
    res = gambaGame.register(ctx.author.name)
    await ctx.send(res)

@bot.command(name="gamba", help="Enter the amount following the command with a space")
async def gamba(ctx):
    try:
        amount = int(ctx.message.content[len("gamba") + 2 :])
        res = gambaGame.gamba(ctx.author.name, amount)
        await ctx.send(res)
    except Exception:
        await ctx.send("Invalid input, please input an integer")

@bot.command(name="check", help="Check how much user has left to gamba")
async def check_amount(ctx):
    res = gambaGame.check(ctx.author.name)
    await ctx.send(res)

@bot.command(name="guess", help="Type the amount and an integer within 1 to 10")
async def guessNum(ctx):
    try:
        amountAndNumS = ctx.message.content[len("guess") + 2 :]
        amountAndNum = amountAndNumS.split()
        amount = int(amountAndNum[0])
        num = int(amountAndNum[1])
        res = gambaGame.numGussing(ctx.author.name, amount, num)
        await ctx.send(res)
    except Exception:
        await ctx.send("Invalid input, please input integers")

bot.run(TOKEN)