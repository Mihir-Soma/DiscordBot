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
    async def bookie(self, ctx):
        users = {}
        active = True
        await ctx.send("*Place your bets!*")

    @commands.command()
    async def bet(self,ctx):
        with open("users.json", "r") as f:
            users = json.loads(f.read())
        if not(ctx.author.id in users):
            users[ctx.author.id] = {"username":ctx.author.name, "nickname":ctx.author.display_name, "guap":10}
            with open("users.json", "w") as f:
                f.write(json.dumps(users))
        await ctx.send('*you have ₲'+ str(users[ctx.author.id]["guap"])+"*")

def setup(bot):
    bot.add_cog(Casino(bot))