import os
import discord
from discord.ext import commands


DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$$$", intents=intents)


@client.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.message.author}")


client.run(DISCORD_TOKEN)