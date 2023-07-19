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

bot.run(TOKEN)