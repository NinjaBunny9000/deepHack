from discord.ext.commands import Bot
from config import discord_token
from utils.logger import logger_mcloggyface as log
import content

prefix = '!'
bot = Bot(command_prefix=prefix, help_command=None)


@bot.event
async def on_ready():
    log.info(f"{bot.user} just booted up! yeet haw!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!howdy'):
        await message.channel.send('partna')

    await bot.process_commands(message)


@bot.command(pass_context=True)
async def test(ctx):
    await ctx.send('NO U!')


@bot.command(pass_context=True, name='help')
async def help_cmd(ctx):
    await ctx.send(content.help_message)


@bot.command(pass_context=True, aliases=['dates'])
async def sched(ctx):
    await ctx.send(content.dates)


@bot.command(pass_context=True)
async def fr(ctx, *, message:str):
    with open('data/features.todo', 'a') as feature_file:
        try:
            feature_file.write(f"\t{message} @{ctx.message.author.name}\n")
            await ctx.send(f'Feature requested: `{message}`')
        except UnicodeEncodeError:
            await ctx.send(f'{ctx.message.author.mention}, try requesting a feature that\'s less... *fancy*.. 🙄')


bot.run(discord_token)