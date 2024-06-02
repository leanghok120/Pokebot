import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import get_pokemon
from keep_alive import import keep_alive

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
    sprite = get_pokemon.get_sprite()
    pokemon_name = get_pokemon.get_name()
    await ctx.send(sprite["front_default"])
    await ctx.send(pokemon_name)

keep_alive()
bot.run(TOKEN)
