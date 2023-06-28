# 👾 PyCon 2023 | Discord Bot 

![Python version](https://img.shields.io/badge/python-v3.10-blue)

This exercise designed for understanding best practices for creating discord bot with using Cogs. After this exercise, you will learn:
- How to use cogs to organize your commands and events
- How to use slash commands
- How to create bot class nad cogs class
- How to use `setup_hook` for syncing commands
- How to create command trees

You can find more information about Cogs in the official docs: https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html#ext-commands-cogs

# Cogs Exercise 1
## Goal:
### 1. Create create a class that has same function as `/hello`, where you implemented for Basics Exercise 1. Create it under `cogs/message.py`
Remember to use:
- app_commands: https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f
- interaction from `discord.Interaction`: https://discordpy.readthedocs.io/en/latest/interactions/api.html
- setup function to add message cog
- when adding cog, using guild parameter with your guild id. You can see below how to get your guild id
![](https://file.notion.so/f/s/b1866199-de54-40b6-ae71-4a47deab9042/Screenshot_2023-06-25_at_17.43.48.png?id=2a1ee61a-9abc-4daa-bf52-0ec5874b2912&table=block&spaceId=c5cd7f93-6861-42b7-bafd-4d0239c7cdae&expirationTimestamp=1688040918252&signature=y7qb4Ik0b8-JrL5PZ9mej9mcxcM-i9dIcMDxy5KmBdA&downloadName=Screenshot+2023-06-25+at+17.43.48.png)

### 2. Create your bot class in `cogs-ex-2.py` and sync your commands. Also, add on_ready functionality into the class to check if everything is fine
Remember to use:
- `setup_hook` for syncing commands
- loading cogs before syncing
- intents setup for the bot class
