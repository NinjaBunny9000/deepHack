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
    await ctx.send(content.help_msg)


@bot.command(pass_context=True, aliases=['dates'])
async def sched(ctx):
    await ctx.send(content.dates)


@bot.command(pass_context=True)
async def fr(ctx, *, message:str):
    try:
        with open('data/features.todo', 'ab') as feature_file:
            feature_request = f"\t☐ {message} @{ctx.message.author.name}\n".encode("utf8")
            feature_file.write(feature_request)
        await ctx.send(f'Feature requested: `{message}`')
    except UnicodeEncodeError:
        await ctx.send(f'YOU SOMEHOW STILL BROKE THE THING, {ctx.message.author.mention}! \
            Try requesting a feature that\'s less... *fancy*.. xD')

@bot.command(pass_context=True)
async def requests(ctx):
    requests = open('data/features.todo', 'rb')
    requests = requests.read().decode("utf8")
    requests = requests.split('requested features:')
    requests = requests[1]
    requests = requests.replace('    ', '').replace('☐ ', '- ').replace('\t', '').replace('\r', '')
    print(repr(requests))
    await ctx.send(f"```markdown\n# REQUESTED FEATURES:\n{requests}```")


@bot.group()
async def challenge(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Command format: `!challenge new <name> <link>`")

@challenge.command()
async def new(ctx, name: str, link: str):
    await ctx.send(f"Challenge {name} created. Link: {link}")
    # add challenge to a list of challenges
    # create a text channel using challenge name
    # set the channel description to use the name as the link
    # create a voice channel
    # inform PM's that a new challenge was created



bot.run(discord_token)