import discord
from discord.ext import commands
import random
import time
import asyncio

com = discord.ext.commands

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix=':)', description=description)

cogs = ['cogs.TicTacToe', 'cogs.Casino']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for c in cogs:
        try:
            bot.load_extension(c)
            print('Loaded {}'.format(c))
        except Exception:
            print('Failed to load {}'.format(c))

@bot.event
async def on_message(msg):
    if msg.author != 748708106011279370:
        if msg.content.startswith('poop'):
            await msg.channel.send('shid')
    await bot.process_commands(msg)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def unload(ctx, cog:str):
    try:
        bot.unload_extension(cog)
        await ctx.send('{} unloaded!'.format(cog))
        
    except Exception:
        await ctx.send('{} failed to unload'.format(cog))

@bot.command()
@commands.has_permissions(manage_guild=True)
async def reload(ctx, cog:str):
    try:
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await ctx.send('{} reloaded!'.format(cog))

    except com.ExtensionAlreadyLoaded:
        await ctx.send('{} already loaded!'.format(cog))

    except com.ExtensionNotFound:
        await ctx.send('{} not found!'.format(cog))

    except com.ExtensionFailed:
        await ctx.send('{} failed to load!'.format(cog))

@bot.command()
@commands.has_permissions(manage_guild=True)
async def load(ctx, cog:str):
    try:
        bot.load_extension(cog)
        await ctx.send('{} loaded!'.format(cog))

    except com.ExtensionAlreadyLoaded:
        await ctx.send('{} already loaded!'.format(cog))

    except com.ExtensionNotFound:
        await ctx.send('{} not found!'.format(cog))

    except com.ExtensionFailed:
        await ctx.send('{} failed to load!'.format(cog))
    
    except Exception:
        await ctx.send('{} failed to load!'.format(cog))

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
async def hermesConrad(ctx):
    swtSmthSmplc=['Sweet llamas of the Bahamas!', 'Sweet lion of Zion!',
                  'Sweet three-toed sloth of Ice Planet Hoth!','Sweet bongo of the Congo!',
                  'Sweet Yeti of the Serengeti! Shes gone crazy-eddy in the headdy!',
                  'Sweet guinea pig of Winnipeg!','Sweet gorilla of Manilla!',
                  'Sweet manatee of Gallilee!','Sweet giant anteater of Santa Anita!','Sweet squid of Madrid!',
                  'Great cow of Moscow!','S-s-s-s-s-sweet something of......someplace.','Sweet ghost of Babylon!', 
                  'Sacred boa of West and East Samoa!', 'Sacred hog of Prague!', 'Cursed bacteria of Liberia!', 
                  'Great bonda of Uganda!','Sweet honey bee of infinity!','Sweet fireball on Montreal!','Sweet kookaburra of Edinburgh!',
                  'Sweet topology of cosmology!','Sweet coinidence of Port-au-Prince!','Sweet freak of Mozambique!',
                  'Sweet orca of Mallorca!', 'Sweet she-cattle of Seattle!']
    random.seed(time.time())
    await ctx.send('*"'+random.choice(swtSmthSmplc)+'"*'+'-Hermes Conrad')

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