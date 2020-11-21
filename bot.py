#downloaded-modules
import discord
from discord.ext import commands

#self-made modules
import ascii_art
import reddit_api
import crypt

#bot token and client object
TOKEN = ''
client = commands.Bot(command_prefix = 'plox ')

client.remove_command('help')

#ascii_art commands
@client.command()
async def sus(ctx):
	response = ascii_art.AmongUs.sus()
	await ctx.send(response)

@client.command()
async def impostor(ctx, name):
    response = ascii_art.AmongUs.isImpostor(name)
    await ctx.send(response)

@client.command()
async def asciiart(ctx, *args):
	name = ' '.join(args)
	result = ascii_art.AsciiTextArt.text_art(name)
	await ctx.send(result)

#reddit_api commands
@client.command()
async def meme(ctx, subreddit: str = ""):
	response = reddit_api.meme(subreddit)
	name = response.title
	url = response.url
	em = discord.Embed(title = name)
	em.set_image(url = url)
	await ctx.send(embed = em)

#crypt commands
@client.command()
async def caesar(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'List of decrypted strings')
	for i in range (1, 27):
		result = crypt.decryption.caeserCipher(string, i)
		embed.add_field(name = str(i), value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def vigenere(ctx, string: str = "", key: str = ""):
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed.set_author(name='Decrypted string')
    result = crypt.decryption.vigenereCipher(string, key)
    embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
    await ctx.send(embed = embed)

@client.command()
async def morse(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
        colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.morseCode(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def tap(ctx, string: str = ""):
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.tapCode(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def ascii(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.ascii(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def bin(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.binary(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def oct(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.octal(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def hex(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.hexadecimal(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def b16(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.base16(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def b32(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.base32(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def b64(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.base64(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

@client.command()
async def b85(ctx, *args):
	string = ' '.join(args)
	embed = discord.Embed(
		colour = discord.Colour.purple())
	embed.set_author(name = 'Decrypted string')
	result = crypt.decryption.base85(string)
	embed.add_field(name = 'Result', value = "`" + result + "`", inline = False)
	await ctx.send(embed = embed)

#general commands
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'({error}), use `plox help` for usage')

@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red())
    embed.set_author(name = 'Help : list of commands available')
    embed.add_field(name = 'cryption', value = 'list of available decryption techniques', inline = False)
    embed.add_field(name = 'misc', value = 'list of miscellaneous commands', inline = False)
    embed.add_field(name = 'info', value = 'information about **cryptobot**', inline = False)
    await ctx.send(embed = embed)

@client.command(pass_context = True)
async def cryption(ctx):
	embed = discord.Embed(
		colour = discord.Colour.red())
	embed.set_author(name = 'Crypt: list of available decryption techniques')
	embed.add_field(name = 'caesar', value = 'returns bruteforce decrypted string using **caesar cipher**', inline = False)
	embed.add_field(name = 'vigenere', value = 'takes a key and returns decrypted string using **vigenere cipher**', inline = False)
	embed.add_field(name = 'morse', value = 'returns decrypted string using **morse code**', inline = False)
	embed.add_field(name = 'tap', value = 'returns decrypted string using **tap code**', inline = False)
	embed.add_field(name = 'bin', value = 'converts **binary** to **decimal**', inline = False)
	embed.add_field(name = 'oct', value = 'converts **octal** to **decimal**', inline = False)
	embed.add_field(name = 'hex', value = 'converts **hexadecimal** to **decimal**', inline = False)
	embed.add_field(name = 'b16', value = 'returns decrypted string using **Base 16**', inline = False)
	embed.add_field(name = 'b32', value = 'returns decrypted string using **Base 32**', inline = False)
	embed.add_field(name = 'b64', value = 'returns decrypted string using **Base 64**', inline = False)
	embed.add_field(name = 'b85', value = 'returns decrypted string using **Base 85**', inline = False)
	await ctx.send(embed = embed)

@client.command(pass_context = True)
async def misc(ctx):
	embed = discord.Embed(
		colour = discord.Colour.blue())
	embed.set_author(name = 'Misc: list of miscellaneous commands')
	embed.add_field(name = 'sus', value = 'returns ascii art of `among us` character', inline = False)
	embed.add_field(name = 'impostor', value = 'returns customized impostor ascii art', inline = False)
	embed.add_field(name = 'asciiart', value = 'returns asciiaart of provided string', inline = False)
	embed.add_field(name = 'meme', value = 'returns a meme from a provided subreddit (dankmemes is default)', inline = False)
	await ctx.send(embed = embed)

@client.command(pass_context = True)
async def info(ctx):
	embed = discord.Embed(
		colour = discord.Colour.green())
	embed.set_author(name = 'Cryptobot')
	embed.add_field(name = 'What is it?', value = '**Cryptobot** is an all-in-one bot made using python, developed by `cryptocrats`', inline = False)
	embed.add_field(name = 'Hosting', value = 'Currently hosted on `Heroku`, cryptobot is under development stage.', inline = False)
	embed.add_field(name = 'Author', value = 'Developed by `Devansh`, member of **cryptocrats**')
	embed.add_field(name = 'Visit', value = 'Souce code can be found here: https://github.com/crypto-crats/discord-bot', inline = False)
	await ctx.send(embed = embed)

client.run(TOKEN)