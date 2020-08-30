import discord
from discord.ext import commands
import random
import time
import asyncio

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
    random.seed(time.time())
    await ctx.send(random.choice(gayGifs))

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

@bot.command()
async def ticTacToe(ctx):
    board=[
           [0,0,0],
           [0,0,0],
           [0,0,0]
        ]
    reacts=[
            ['1️⃣','2️⃣','3️⃣'],
            ['4️⃣','5️⃣','6️⃣'],
            ['7️⃣','8️⃣','9️⃣']
        ]
    win=0
    trn=0
    while True: 
        #prints out board
        for count,i in enumerate(board):
            s=''
            for j in i:
                if j == 0:
                    s+='⬜'
                elif j == 1:
                    s+='❌'
                else:
                    s+='⭕'
            m=await ctx.send(s)
            for r in reacts[count]:
                await m.add_reaction(r)
        await ctx.send('------------------------')
        
        # displays win message
        if win==1:
            await ctx.send('*you win 😔*')
            break
        if win==2:
            await ctx.send('*I win 💩*')
            break
        
        # next turn button
        if trn%2 != 0:
            nt=await ctx.send('next turn')
            await nt.add_reaction('👉')
        
        # check reactions
        def check(reaction, user):
            return user == ctx.author

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            win=2
        
        # bot's turn
        b2=[]
        if trn%2!=0:
            for count,i in enumerate(board):
                for cnt,j in enumerate(i):
                    if j==0:
                        b2.append((count,cnt))
            x,y=random.choice(b2)
            board[x][y]=2
            trn+=1     

        # user's turn 
        elif trn%2==0:
            for count,i in enumerate(reacts):
                for cnt,j in enumerate(i):
                    if reaction.emoji == j and board[count][cnt]==0:
                        board[count][cnt]=1
                        trn+=1
                    elif reaction.emoji == j and board[count][cnt]!=0:
                        await ctx.send('*choose an open space*')

        # win conditions
        for i in board:
            if i[1]==i[0] and i[2]==i[0] and i[0]!=0:
                if i[0]==1:
                    win=1
                else:
                    win=2
        for i in range(0,2):
            if board[0][i]==board[1][i] and board[0][i]==board[2][i] and board[0][i]!=0:
                if board[0][i]==1:
                    win=1
                else:
                    win=2
        if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!=0:
            if board[0][0]==1:
                win=1
            else:
                win=2     
        if board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!=0:
            if board[0][2]==1:
                win=1
            else:
                win=2                 

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