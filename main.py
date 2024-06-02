import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Get app token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Pokebot is online!")


bot.run(TOKEN)
