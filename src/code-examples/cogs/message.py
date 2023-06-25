import os
import discord
from discord.ext import commands
from discord import app_commands


GUILD_ID = int(os.environ["GUILD_ID"])


class Message(commands.Cog, name="message"):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello_v2", description="Bot says hello to you")
    async def hello_v2(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.name}!")


async def setup(bot: commands.Bot):
    await bot.add_cog(Message(bot), guild=discord.Object(id=GUILD_ID))
