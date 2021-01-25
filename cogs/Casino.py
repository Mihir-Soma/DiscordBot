import discord
import time
import asyncio
import json
import os
from discord.ext import commands


class Casino(commands.Cog):
    active = False
    bets = []

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def register(self,ctx):
        with open("users.json", "r") as f:
            users = json.load(f)
        authorid=str(ctx.author.id)

        if authorid not in users:
            users[authorid] = {"username":ctx.author.name, "nickname":ctx.author.display_name, "guap":10}
            with open("users.json", "w") as f:
                json.dump(users, f)
            await ctx.send("*thank you for registering, " + "<@!" + authorid + ">!*")
        else:
            await ctx.send("*you are already registered!*")

    @commands.command()
    async def bookie(self, ctx):
        '''
        users = {}
        active = True
        await ctx.send("*Place your bets!*")
        '''

    @commands.command()
    async def balance(self,ctx):
        with open("users.json", "r") as f:
            users = json.load(f)
        authorid = str(ctx.author.id)
        await ctx.send("<@!" + authorid + '>*you have ₲'+ str(users[authorid]["guap"])+"*")

    @commands.command()
    async def bet(self,ctx,amount: int):
        with open("users.json", "r") as f:
            users = json.load(f)
        authorid=str(ctx.author.id)

        if amount <= users[authorid]["guap"] and amount > 0:
            await ctx.send("<@!" + authorid + '>*, your bet is ' + str(amount) + "*")
            users[authorid]["guap"]-=amount
            await ctx.send(users[authorid]["guap"])
            with open("users.json", "w") as f:
                json.dump(users, f)
        else:
            await ctx.send("*you don't have enough Guap*")
        

def setup(bot):
    bot.add_cog(Casino(bot))