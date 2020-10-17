import discord
import among_us
from discord.ext import commands

TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = 'plox ')

client.remove_command('help')

@client.command()
async def sus(ctx):
	response = among_us.sus()
	await ctx.send(response)

@client.command()
async def impostor(ctx, name):
    response = among_us.isImpostor(name)
    await ctx.send(response)

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'({error}), use `plox help` for usage')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='sus', value='ascii art of `Among Us` character', inline=False)
    embed.add_field(name='impostor', value='takes a single value and returns ascii art of impostor', inline=False)
    await ctx.send(embed=embed)

client.run(TOKEN)