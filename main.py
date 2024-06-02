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
async def rowlett(ctx):
    with open("rowlet.jpg", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


bot.run(TOKEN)
