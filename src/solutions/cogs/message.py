import os
import discord
from discord.ext import commands
from discord import app_commands


GUILD_ID = int(os.environ["GUILD_ID"])


class MessageExercise(commands.Cog, name="message"):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello_exercise", description="Bot says hello to you")
    async def hello_exercise(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello. What is your name?")

        def check(message):
            return message.author == interaction.user

        message = await self.bot.wait_for("message", check=check)
        if message:
            await interaction.followup.send(
                f"Nice to meet you {message.content}. Do you like Python?"
            )
            second_message = await self.bot.wait_for("message", check=check)
            if second_message:
                await interaction.followup.send("Thank you for your input")


async def setup(bot: commands.Bot):
    await bot.add_cog(MessageExercise(bot), guild=discord.Object(id=GUILD_ID))
