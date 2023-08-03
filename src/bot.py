import os
import discord
from discord import Intents
from dotenv import load_dotenv
from discord.ext import commands
import gamba as gambaGame
import magic8ball as magicBall
import gameHandler as gameHandler

# key: users name, value: money
user_data = {}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

INTENTS = discord.Intents.default()
INTENTS.members = INTENTS.messages = INTENTS.message_content = INTENTS.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=INTENTS)

@bot.event
async def on_ready():
    print("Bot is READY!!!")

@bot.listen("on_message")
async def on_message_listen(message):
    if "Hi" in message.content:
        await message.channel.send("Hello :)")

@bot.command(name="luck", help="This tells you your luck for the day!")
async def luck_today(ctx):
    await ctx.send(magicBall.luck())

@bot.command(name="magic8ball", help="Magic 8 ball, try asking it a question!")
async def magic8ball(ctx):
    await ctx.send(magicBall.magic8())

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):       
        await ctx.send("Not a valid command. !commands to see a list of commands!")

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

@bot.command(name="adventure", help="Follow up the command with a number to start that adventure, currently support 1, 2")
async def startAdventure(ctx):
    num = ctx.message.content[len("adventure") + 2 :]
    res = gameHandler.startGame(num)
    await ctx.send(res)

@bot.command(name="direction", help="Command to pick the direction")
async def pickDirection(ctx):
    direction = ctx.message.content[len("direction") + 2 :]
    res = gameHandler.optionPick(direction)
    await ctx.send(res)

bot.run(TOKEN)