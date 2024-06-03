import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import get_pokemon

# Get app token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Pokebot is online!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}!")


@bot.tree.command(name="pokemon")
async def pokemon(interaction: discord.Interaction):
    pokemon_sprite = get_pokemon.get_sprite()
    pokemon_name = get_pokemon.get_name()

    await interaction.response.send_message(
        f"{pokemon_name}: {pokemon_sprite["front_default"]}"
    )


bot.run(TOKEN)
