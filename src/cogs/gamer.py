import discord
from discord.ext import commands


class GammerCogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @discord.app_commands.command(name="hello", description="Bot says hello to you")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.name}!")
        

    @discord.app_commands.command(name="animals", description="Get your favorite animal")
    async def animals(self, interaction: discord.Interaction):
        ctx: commands.Context = await self.bot.get_context(interaction)
        view = discord.ui.View()
        select = discord.ui.Select(options=[
            discord.SelectOption(label='monkey', description='if you like monkey click me', emoji='🐵'),
            discord.SelectOption(label='panda', description='if you like panda click me', emoji='🐼'),
            discord.SelectOption(label='dog', description='if you like monkey click me', emoji='🐶'),
        ])
        async def select_callback(interaction: discord.Interaction):
            await interaction.response.send_message(select.values[0])
        select.callback = select_callback
        view.add_item(select)
        await ctx.send(f"Select your animals", view=view)