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


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")


@bot.command()
async def rowlet(ctx):
    await ctx.send(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/722.png"
    )


bot.run(TOKEN)
