import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from get_pokemon import get_sprite

# Get app token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Pokebot is online!")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")


@bot.command()
async def pokemon(ctx):
    sprite = get_sprite()
    await ctx.send(sprite["front_default"])


bot.run(TOKEN)
