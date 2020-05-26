import discord
from config import discord_token
from utils.logger import logger_mcloggyface as log

client = discord.Client()

@client.event
async def on_ready():
    log.info(f"{client.user} just booted up! yeet haw!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!howdy'):
        await message.channel.send('partna')

client.run(discord_token)