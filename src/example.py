import os
import discord

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])


intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    channel = client.get_channel(CHANNEL_ID)
    print(f"Bot is active as {client.user}")
    await client.change_presence(
        activity=discord.Game(name="Hello!"), status=discord.Status.do_not_disturb
    )
    await channel.send("Bot is active")


client.run(DISCORD_TOKEN)
