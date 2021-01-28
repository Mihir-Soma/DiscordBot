import discord
import time
import asyncio
import random
import json
import os
from discord.ext import commands

active = False
bets = {}    
outcome1 = ""
outcome2 = ""
odds1 = 0
odds2 = 0

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
    async def startBet(self,ctx, o1: str, o2: str):
        global active, outcome1, outcome2
        outcome1 = o1
        outcome2 = o2
        await ctx.send("*place your bets! " + outcome1 + " or " + outcome2 +"?* \n`type :)bookie placeBet <amount> <choice>`")
        active = True

    @bookie.command()
    async def placeBet(self,ctx, amount: int, onChoice: str):
        global active
        with open("users.json", "r") as f:
            users = json.load(f)
        authorid=str(ctx.author.id)

        if active == True and onChoice == (outcome1 or outcome2):
            if amount <= users[authorid]["guap"] and amount > 0:
                users[authorid]["guap"] -= amount
                with open("users.json", "w") as f:
                    json.dump(users, f)
                bets[authorid] = {onChoice: amount}
                await ctx.send(ctx.author.mention + ' *your bet is ' + str(amount) + "* \n*you have ₲" + str(users[authorid]["guap"])+" left*")   

            elif amount > users[authorid]["guap"]:
                await ctx.send("*you don't have enough Guap*")

            else:
                await ctx.send("*invalid bet*")

        elif active == False:
            await ctx.send("*nothing to bet on!*")

    @bookie.command()
    async def odds(self,ctx):
        global odds1, odds2
        for bet in bets:
            for choice in bet[bet]:
                if bets[i] == outcome1:
                    odds1+=bets[bet][choice]
                if bets[i] == outcome2:
                    odds+=best[bet][choice]
        await ctx.send("*the odds are* " + str(odds1) + ":" + str(odds2))

    @bookie.command()
    async def closeBet(self,ctx):
        global active
        await ctx.send("*bets can no longer be placed*")
        active = False

    @bookie.command()
    async def winners(self,ctx, winner: str):
        global outcome1, outcome2
        
        await ctx.send("")

def setup(bot):
    bot.add_cog(Casino(bot))