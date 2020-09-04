
import discord
from discord.ext import tasks, commands
import flask
import os

class mod( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def delete(self, ctx):
        await ctx.channel.purge( limit=5 )

    @commands.command( alias='deletus' )
    @commands.cooldown( 10, per=1 )
    async def clear(ctx, amount=5):
        await ctx.channel.purge( limit=5 )

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def warn(self, ctx, member: discord.Member,*, reason):
        await ctx.channel.trigger_typing()
        embed = discord.Embed(title="WARN", description="You have been warned", color=0xeee657)
        embed.add_field( name="User:", value=f'you have been warned {member.mention}', inline=False )
        embed.add_field( name="Reasoning", value=f'reason: {reason}', inline=False )
        await ctx.send(embed=embed)
        await member.send( 'yo stop being bad and breaking the rules' )
        await member.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def dmspam(self, ctx, member: discord.Member):
        for i in range(500):
            await member.send( 'yo stop being bad and breaking the rules' )



def setup(bot):
    bot.add_cog( mod( bot ) )
