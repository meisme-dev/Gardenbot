import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
from datetime import datetime

class Moderation(commands.Cog):

    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(administrator=True)
    async def kick(self,ctx,member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f':white_check_mark: | The member {member.mention} has been kicked off this server.')

def setup(bot):
    bot.add_cog(Moderation(bot))
