import discord
from discord.ext import tasks, commands
import flask
import os
from discord import *
from discord.ext import *

class flask( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def graph(self,ctx,a):
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace( -5, 5, 100 )
        plt.plot( x, y, '-r', label=y )
        plt.title( 'Graph of y=2x+1' )
        plt.xlabel( 'x', color='#1C2833' )
        plt.ylabel( 'y', color='#1C2833' )
        plt.legend( loc='upper left' )
        plt.grid()
        plt.savefig('plot.png')
        await ctx.send( file=discord.File('plot.png' ) )
    @commands.command(pass_context = True)
    async def nickchange(self, ctx, a):
        b = ctx.message.author.name
        await ctx.send(f'changing {b} nickname on server to {a}')
        await ctx.message.author.edit( nick=a )
    @commands.command()
    async def pfp(self,ctx, member: discord.Member ):
        profile_location= r"F:\the desktop\UglyBot(new)\databases\profile\pfp.png"
        file2=profile_location
        member.avatar_url_as( format="png" ).save( fp=profile_location )
        await ctx.send(f'{member} profile picture')
        await ctx.send(file=discord.File(profile_location))
    @commands.command()
    async def userinfo(self,ctx,member:discord.Member):
        await member.send(
            'someone has requested your info, although this is public, we like to let users know as we belive it is there right')
        discord_user_id = member.id
        discord_user_age = member.created_at
        embed = discord.Embed(title="USER INFO", description=f"User Info For {member}:", color=0xeee657)
        embed.add_field(name="User Id", value=discord_user_id, inline= False)
        embed.add_field(name="Account Created At", value=discord_user_age,inline=False)
        embed.add_field(name="Account Type", value='User Account', inline=False)
        await ctx.send(embed=embed)
        profile_location = r"F:\the desktop\UglyBot(new)\databases\profile\pfp.png"
        file2 = profile_location
        member.avatar_url_as( format="png" ).save( fp=profile_location )
        await ctx.send( f'{member} profile picture' )
        await ctx.send( file=discord.File( profile_location ) )
def setup(bot):
    bot.add_cog( flask( bot ) )
