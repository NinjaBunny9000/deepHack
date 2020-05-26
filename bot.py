from discord.ext.commands import Bot
from config import discord_token
from utils.logger import logger_mcloggyface as log

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
    response = """```markdown
# Here's what works so far..
!help - this thing
!fr <feature> - request a feature for the bot
!sched/!dates - important dates

# These commands are in development..
<none>
```"""
    await ctx.send(response)


@bot.command(pass_context=True, aliases=['dates'])
async def sched(ctx):
    response = """```markdown
# Important dates:
● Top Ten Final Event Applications Due: June 4, 2020, 8:00pm (EDT)
● Qualification Event Top Ten Technical Papers Due: June 14, 2020, 8:00pm (EDT)
● Top Ten Final Event Invitations sent: June 24, 2020
● Final Event Start: August 7, 2020, 10:00am (EDT)
● Final Event Conclusion: August 9, 2020, 12:00pm (EDT)
● Final Event Top Ten Technical Papers Due: August 30, 2020, 8:00pm (EDT)```"""
    await ctx.send(response)


@bot.command(pass_context=True)
async def fr(ctx, *, message:str):
    with open('data/features.todo', 'a') as feature_file:
        try:
            feature_file.write(f"\t{message} @{ctx.message.author.name}\n")
            await ctx.send(f'Feature requested: `{message}`')
        except UnicodeEncodeError:
            await ctx.send(f'{ctx.message.author.mention}, try requesting a feature that\'s less... *fancy*.. 🙄')


bot.run(discord_token)