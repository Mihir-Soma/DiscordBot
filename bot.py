import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix=':)', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(msg):
    if msg.author != 748708106011279370:
        if msg.content.startswith('poop'):
            await msg.channel.send('shid')
    await bot.process_commands(msg)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def gay(ctx):
    gayGifs=['https://tenor.com/view/trolling-iam-homophobic-madden-gif-16547625', 'https://tenor.com/view/twitch-xqc-suck-gif-13965169', 
             'https://tenor.com/view/tyler-oakley-yay-gay-lgbt-gay-gif-4322816', 'https://tenor.com/view/homophobic-rock-lee-homophobic-mode-naruto-gif-18125915', 
             'https://media.giphy.com/media/m7e07TZRV20Xm/giphy.gif', 'https://media.giphy.com/media/89asT84PzDwwE/giphy.gif', 
             'https://tenor.com/view/fall-pass-out-tired-exhausted-dennis-gif-17764286', 'https://tenor.com/view/michael-the-office-gif-5323535']
    await ctx.send(random.choice(gayGifs))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
bot.run('NzQ4NzA4MTA2MDExMjc5Mzcw.X0hWwg.V4ziGJE_eOJ3TzSzACrYIFOorEs')