import discord
import random
from discord.ext import commands

TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '~')

client.remove_command('help')

@client.command()
async def now(ctx):
	response = 'Currently in development stage'
    await ctx.send(response)

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'({error}), use ~help for usage')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='~now', value='Gives current state of the bot', inline=False)
    await ctx.send(embed=embed)

client.run(TOKEN)