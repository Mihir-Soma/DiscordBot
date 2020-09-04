import discord
import random
import time
import asyncio
from discord.ext import commands


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticTacToe(self, ctx):
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
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
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
def setup(bot):
    bot.add_cog(TicTacToe(bot))