import os
import discord
from discord.ext import commands

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready() -> None:
    print("Bot is active")
    channel = bot.get_channel(CHANNEL_ID)
    await bot.change_presence(
        activity=discord.Game(name="Hello!"), status=discord.Status.do_not_disturb
    )
    await channel.send("Bot is active")


@bot.command()
async def hello(ctx) -> None:
    await ctx.send("Hello")


@bot.command()
async def reaction(ctx) -> None:
    await ctx.send("React this message with 👍")

    def check(reaction, user):
        return user != bot.user and str(reaction.emoji) == "👍"

    reaction, user = await bot.wait_for("reaction_add", check=check)
    if reaction:
        await ctx.send(f"Thank you for your reaction {user}")


bot.run(DISCORD_TOKEN)
