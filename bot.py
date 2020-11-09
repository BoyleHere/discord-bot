#downloaded-modules
import discord
from discord.ext import commands

#self-made modules
import ascii_art
import reddit_api

#bot token and client object
TOKEN = ''
client = commands.Bot(command_prefix = 'plox ')

client.remove_command('help')

@client.command()
async def sus(ctx):
	response = ascii_art.AmongUs.sus()
	await ctx.send(response)

@client.command()
async def impostor(ctx, name):
    response = ascii_art.AmongUs.isImpostor(name)
    await ctx.send(response)

@client.command()
async def ascii(ctx, name):
    response = ascii_art.AsciiTextArt.text_art(name)
    await ctx.send(response)

@client.command()
async def meme(ctx, subreddit: str = ""):
	response = reddit_api.meme(subreddit)
	name = response.title
	url = response.url
	em = discord.Embed(title = name)
	em.set_image(url = url)
	await ctx.send(embed = em)

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
    embed.add_field(name='meme', value='takes a single or no value, returns meme from the subreddit', inline=False)
    embed.add_field(name='ascii', value='ascii art of given value', inline=False)
    await ctx.send(embed=embed)

client.run(TOKEN)