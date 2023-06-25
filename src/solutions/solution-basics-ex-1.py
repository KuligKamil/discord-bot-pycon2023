import os
import discord
from discord.ext import commands

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready() -> None:
    print(f"Bot is active {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Bot is active")


@bot.command()
async def hello(ctx) -> None:
    await ctx.send(f"Hello. What is your name?")

    def check(message):
        return message.author == ctx.author

    message = await bot.wait_for("message", check=check)
    if message:
        await ctx.send(f"Nice to meet you {message.content}. Do you like Python?")
        second_message = await bot.wait_for("message", check=check)
        if second_message:
            await ctx.send("Thank you for your input")


bot.run(DISCORD_TOKEN)
