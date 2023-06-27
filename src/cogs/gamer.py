import random
import discord
from discord.ext import commands


class GammerCogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.games = ["FIFA", "LOL", "THE SIMS"]

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

    
    @discord.app_commands.command(name="games", description="Help you to choose which game you want to play")
    async def games(self, interaction: discord.Interaction):
        ctx: commands.Context = await self.bot.get_context(interaction)
        view = discord.ui.View()
        options = [discord.SelectOption(label=game, description=f"Pick this if like {game}!") for game in self.games]
        select = discord.ui.Select(    
            placeholder = "Choose your game!",
            min_values = 2,
            max_values = len(options),
            options = options)
        async def select_callback(interaction: discord.Interaction):
            chosen_game = random.choice(select.values)
            await interaction.response.send_message(chosen_game)
        select.callback = select_callback
        view.add_item(select)
        await ctx.send(f"Select your games", view=view)


    @discord.app_commands.command(name="game", description="Select game")
    async def game(self, interaction: discord.Interaction):
        ctx: commands.Context = await self.bot.get_context(interaction)
        view = discord.ui.View()
        buttons = [discord.ui.Button(label=game) for game in self.games]
        async def callback(interaction: discord.Interaction):
            # how to get value from button ?
            await interaction.response.send_message()
        for button in buttons:
            button.callback = callback
            view.add_item(button)
        await ctx.send(f"Select your games", view=view)