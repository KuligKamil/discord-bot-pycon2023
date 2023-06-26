import discord
from discord.ext import commands


class GammerCogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @discord.app_commands.command(name="hello", description="Bot says hello to you")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.name}!")
