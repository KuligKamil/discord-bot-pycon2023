import random

import discord
from discord.ext import commands

games = ["FIFA", "LOL", "THE SIMS"]

class NewGame(discord.ui.Modal, title='New Game'):

    name = discord.ui.TextInput(
        label='Name',
        placeholder='Type name here...',
        min_length=3,
        max_length=50
    )

    async def on_submit(self, interaction: discord.Interaction):
        games.append(self.name.value)
        await interaction.response.send_message(f'Thanks for your for adding new game, {self.name.value}!', ephemeral=True)


class Vue(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="hello-button-2", custom_id="hello-button-2", style=discord.ButtonStyle.red)
    async def hello_button_2(self, interaction, button: discord.Button):
        await interaction.response.send_message("HOLA")


class CounterView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="0", custom_id="counter", style=discord.ButtonStyle.green)
    async def counter_button(self, interaction, button: discord.Button):
        button.label = str(int(button.label) + 1)
        await interaction.response.edit_message(view=self)


class VoteButton(discord.ui.Button):
    def __init__(self, label: str):
        super().__init__(label=label)
    
    async def callback(self, interaction: discord.Interaction):
        if interaction.user.name in self.view.users:
            await interaction.response.send_message(f"Don't cheat. {interaction.user}")
        else: 
            await interaction.response.send_message(f"User {interaction.user}. Choose: {self.label}")
            self.view.results[self.label] = self.view.results[self.label] + 1
            self.view.users.append(interaction.user.name)
        return await super().callback(interaction)


class VoteView(discord.ui.View):
    users = []
    results = {}
    def __init__(self):
        super().__init__()
        for game in games:
            self.results[game] = 0
            self.add_item(VoteButton(label=game))

    

class GammerCogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="hello", description="Bot says hello to you")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.name}!")


    @discord.app_commands.command(name="hello-button", description="Bot says hello to you")
    async def hello_button(self, interaction: discord.Interaction):
        view = discord.ui.View()
        button = discord.ui.Button(label='hello', custom_id='hello', style=discord.ButtonStyle.red)
        async def button_callback(interaction: discord.Interaction):
            await interaction.response.send_message('hi')
        button.callback = button_callback
        view.add_item(button)
        await interaction.response.send_message(view=view)
    

    @discord.app_commands.command(name="hello-button-2", description="Bot says hello to you")
    async def hello_button_2(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=Vue())

    
    @discord.app_commands.command(name="counter")
    async def counter(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=CounterView())


    @discord.app_commands.command(name="animals", description="Get your favorite animal")
    async def animals(self, interaction: discord.Interaction):
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
        await interaction.response.send_message(f"Select your animals", view=view)

    
    @discord.app_commands.command(name="games", description="Help you to choose which game you want to play")
    async def games(self, interaction: discord.Interaction):
        view = discord.ui.View()
        options = [discord.SelectOption(label=game, description=f"Pick this if like {game}!") for game in games]
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
        await interaction.response.send_message(f"Select your games", view=view)

    
    @discord.app_commands.command(name="vote-for-game", description="Select game")
    async def vote(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Select to want play", view=VoteView())


    @discord.app_commands.command(name="add-new-game", description="Select game")
    async def new_game(self, interaction: discord.Interaction):
        await interaction.response.send_modal(NewGame())
