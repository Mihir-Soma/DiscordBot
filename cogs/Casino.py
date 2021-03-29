import discord
import time
import asyncio
import random
import json
import os
from fractions import Fraction
from discord.ext import commands

active = 0
bets = {}    
outcome1 = ""
outcome2 = ""
pool1 = 0
pool2 = 0

class Casino(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #registers a new gambler
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

    #returns the users balance
    @commands.command()
    async def balance(self,ctx):
        with open("users.json", "r") as f:
            users = json.load(f)
        authorid = str(ctx.author.id)
        await ctx.send(ctx.author.mention + '*you have ₲'+ str(users[authorid]["guap"])+"*")

    #helper function to add guap to a user's balance
    def addGuap(self, amnt: int, authorid: str):
        with open("users.json", "r") as f:
            users = json.load(f)
        users[authorid]["guap"]+=amnt
        with open("users.json", "w") as f:
            json.dump(users, f)

    #group of commands used to bet
    @commands.group()
    async def bookie(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("*invalid bookie command*")

    #initiates a bet with two outcomes
    @bookie.command()
    async def startBet(self,ctx, o1: str, o2: str):
        global active, outcome1, outcome2, pool1, pool2
        if active == 0:
            active = 1
            pool1 = 0
            pool2 = 0
            outcome1 = o1
            outcome2 = o2
            await ctx.send("*place your bets! " + outcome1 + " or " + outcome2 +"?* \n`type :)bookie placeBet <amount> <choice>`")
        else: 
            await ctx.send("*a bet is already active*")

    #helper function which returns the odds in outcome1:outcome2 form
    def odd(self):
        global bets, pool1, pool2
        pool1 = 0
        pool2 = 0
        for user in bets:
            if bets[user][0] == outcome1:
                pool1+=bets[user][1]
            else:
                pool2+=bets[user][1]
        odds = Fraction(pool1, pool2)
        return odds
    
    @bookie.command()
    async def odds(self,ctx):
        await ctx.send("*the odds are " + str(self.odd().numerator) + ":" + str(self.odd().denominator) + "*")

    #takes a bet from a user and subtracts it from their balance
    @bookie.command()
    async def placeBet(self,ctx, amount: int, onChoice: str):
        global active
        with open("users.json", "r") as f:
            users = json.load(f)
        authorid=str(ctx.author.id)
        if authorid not in users:
            await ctx.send("*please register using* `:)register`")
        elif authorid in bets:
            await ctx.send("***you already placed a bet!*** *dumbass*")
        elif active == 1 and (onChoice == outcome1 or onChoice == outcome2):
            if amount <= users[authorid]["guap"] and amount > 0:
                users[authorid]["guap"] -= amount
                with open("users.json", "w") as f:
                    json.dump(users, f)               
                bets[authorid] = (onChoice, amount) 
                await ctx.send(ctx.author.mention + ' *your bet is ₲' + str(amount) + "* \n*you have ₲" + str(users[authorid]["guap"])+" left*")
                await ctx.send("*the new odds are " + str(self.odd().numerator) + ":" + str(self.odd().denominator) + "*")

            elif amount > users[authorid]["guap"]:
                await ctx.send("*you don't have enough Guap*")

            else:
                await ctx.send("*invalid bet*")

        elif active == 0:
            await ctx.send("*nothing to bet on!*")
        elif active == 2:
            await ctx.send("*the bet is already closed*")
        else:
            await ctx.send("*that's not a choice*")
    
    #closes the bet
    @bookie.command(aliases = ["CloseBet", "closebet", "Closebet"])
    async def closeBet(self,ctx):
        global active
        await ctx.send("*bets can no longer be placed*")
        active = 2

    #ends the bet and pays out gamblers
    @bookie.command()
    async def endBet(self,ctx, winner: str):
        global outcome1, outcome2, pool1, pool2, bets
        if winner == outcome1:
            coef = pool2/pool1
        else:
            coef = pool1/pool2

        for user in bets:
            if bets[user][0] == winner:
                profit = int(bets[user][1]*coef)
                self.addGuap(profit+bets[user][1], user)
                await ctx.send("<@!" + user + "> *earned " + str(profit+bets[user][1]) + "*")

def setup(bot):
    bot.add_cog(Casino(bot))