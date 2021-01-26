import discord
import time
import asyncio
import random
import json
import os
from discord.ext import commands

active = False
bets = {}    

class Casino(commands.Cog):
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
            await ctx.send("*thank you for registering, " + ctx.author.mention + "!")
        else:
            await ctx.send("*you are already registered!*")

    @commands.command()
    async def balance(self,ctx):
        with open("users.json", "r") as f:
            users = json.load(f)
        authorid = str(ctx.author.id)
        await ctx.send(ctx.author.mention + '* you have ₲'+ str(users[authorid]["guap"])+"*")

    @commands.group()
    async def bookie(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("*invalid bookie command*")
         
    @bookie.command()
    async def startBet(self,ctx, outcome1: str, outcome2: str):
        await ctx.send("*place your bets! " + outcome1 + " or " + outcome2 +"?*")
        active = True
        await ctx.send(str(active))

    @bookie.command()
    async def placeBet(self,ctx, amount: int, onChoice: str):
        with open("users.json", "r") as f:
            users = json.load(f)
        authorid=str(ctx.author.id)
        await ctx.send(str(active))
        if active == True:
            if amount <= users[authorid]["guap"] and amount > 0:
                await ctx.send(ctx.author.mention + ' *your bet is ' + str(amount) + "*")
                users[authorid]["guap"]-=amount
                await ctx.send(users[authorid]["guap"])
                with open("users.json", "w") as f:
                    json.dump(users, f)
                bets[authorid] = {onChoice: amount}
            elif amount > users[authorid]["guap"]:
                await ctx.send("*you don't have enough Guap*")
            else:
                await ctx.send("*invalid bet*")
        elif active == False:
            await ctx.send("*nothing to bet on!*")

    @bookie.command()
    async def closeBet(self,ctx):
        await ctx.send("*bets can no longer be placed*")
        active = False


def setup(bot):
    bot.add_cog(Casino(bot))